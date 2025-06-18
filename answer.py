import argparse
import base64
import os
import json
import numpy as np
import re
from pydantic import BaseModel
import httpx
from pathlib import Path
from dotenv import load_dotenv
from fastapi import FastAPI
import time
from google.genai.types import GenerateContentConfig
from google import genai

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    image: str = None

# ---------- Rate Limiter ----------
class RateLimiter:
    def __init__(self, requests_per_minute=60, requests_per_second=2):
        self.requests_per_minute = requests_per_minute
        self.requests_per_second = requests_per_second
        self.request_time = []
        self.last_request_time = 0

    def wait_if_needed(self):
        current_time = time.time()

        # Per-second rate limit
        time_since_last = current_time - self.last_request_time
        if time_since_last < (1 / self.requests_per_second):
            time.sleep((1 / self.requests_per_second) - time_since_last)

        # Per-minute rate limit
        self.request_time = [t for t in self.request_time if current_time - t < 60]
        if len(self.request_time) >= self.requests_per_minute:
            sleep_time = 60 - (current_time - self.request_time[0])
            if sleep_time > 0:
                time.sleep(sleep_time)
            self.request_time = [t for t in self.request_time if current_time - t < 60]

        self.request_time.append(time.time())
        self.last_request_time = time.time()

# ---------- Setup ----------
rate_limiter = RateLimiter(requests_per_minute=5, requests_per_second=2)
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY not set in environment.")
client = genai.Client(api_key=api_key)

# ---------- Embedding ----------
def get_embedding(text: str, max_retries: int = 3) -> list[float]:
    for attempt in range(max_retries):
        try:
            rate_limiter.wait_if_needed()
            response = client.models.embed_content(
                model="gemini-embedding-exp-03-07",
                contents=text
            )
            return response.embeddings[0].values
        except Exception as e:
            if "rate limit" in str(e).lower() or "quota exceeded" in str(e).lower():
                wait_time = 2 ** attempt
                print(f"Rate limit hit. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            elif attempt == max_retries - 1:
                raise
            else:
                print(f"Retry {attempt + 1} failed: {e}")
                time.sleep(1)
    raise Exception("Max retries exceeded.")

# ---------- Utility ----------
def generate_image_description(image_path):
    file = client.files.upload(file_path=image_path)
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            file,
            "Describe this image in detail, focusing on any text, object or relevant information it contains that could help answer question about it."
        ]
    )
    return response.text

def load_embeddings():
    data = np.load("embedding.npz", allow_pickle=True)
    embeddings = data["embeddings"]
    chunks = data["chunks"]
    return embeddings, chunks

def generate_llm_response(question: str, context: str):
    system_prompt = """
You are a knowledgeable and helpful teaching assistant.

Your task is to answer questions using the provided context only. If the context is insufficient to answer the question accurately, respond with: "I don't know."

Format your answers using Markdown. Use:
- Headings for sections or summaries
- Bullet points or numbered lists where appropriate
- Code blocks (with syntax highlighting if applicable) for code snippets

Be clear, concise, and accurate. Avoid speculation. If multiple interpretations are possible, mention them.

Remember: Do not include information not present in the context.
"""
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[system_prompt, f"Context:\n{context}\n\nQuestion: {question}"],
        config=GenerateContentConfig(temperature=0.5, top_p=0.95, top_k=40)
    )
    return response.text

# ---------- URL Extraction ----------
def extract_url_from_chunk(chunk: str) -> str | None:
    # Try [POST: ...]
    match = re.search(r"\[POST:\s*(https?://[^\]]+)\]", chunk)
    if match:
        return match.group(1)

    # Try [SOURCE: ...]
    match = re.search(r"\[SOURCE:\s*(https?://[^\]]+)\]", chunk)
    if match:
        return match.group(1)

    # Try - https://... under [SOURCE LINKS]
    if "[SOURCE LINKS]" in chunk:
        match = re.search(r"-\s*(https?://[^\s]+)", chunk)
        if match:
            return match.group(1)

    return None

# ---------- Main Answer Function ----------
def answer(question: str, image: str = None):
    embeddings, chunks = load_embeddings()

    if image:
        image_description = generate_image_description(f"data:images/jpeg;base64,{image}")
        question += f" {image_description}"

    question_embedding = get_embedding(question)
    similarities = np.dot(
        embeddings, question_embedding
    ) / (np.linalg.norm(embeddings, axis=1) * np.linalg.norm(question_embedding))

    top_indices = np.argsort(similarities)[-10:][::-1]
    top_chunks = [chunks[i] for i in top_indices]

    reference_url = extract_url_from_chunk(top_chunks[0])
    response = generate_llm_response(question, "\n\n".join(top_chunks))

    return {
        "question": question,
        "response": response,
        "reference_url": reference_url
    }

# ---------- API Endpoint ----------
@app.post("/api/")
async def api_answer(request: QuestionRequest):
    try:
        return answer(request.question, request.image)
    except Exception as e:
        return {"error": str(e)}

# ---------- Local Run ----------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
