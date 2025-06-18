import os
import re
import time
import json
import numpy as np
from pathlib import Path
from tqdm import tqdm
from dotenv import load_dotenv
from semantic_text_splitter import MarkdownSplitter
import vertexai
from vertexai.language_models import TextEmbeddingInput, TextEmbeddingModel

# --- Load environment variables ---
load_dotenv()
PROJECT_ID = "teak-strength-463307-b0"
LOCATION = "us-central1"
EMBEDDING_MODEL_NAME = "gemini-embedding-001"
TASK_TYPE = "SEMANTIC_SIMILARITY"

vertexai.init(project=PROJECT_ID, location=LOCATION)
embedding_model = TextEmbeddingModel.from_pretrained(EMBEDDING_MODEL_NAME)

# --- Rate limiter ---
class RateLimiter:
    def __init__(self, requests_per_minute=500, requests_per_second=10):
        self.requests_per_minute = requests_per_minute
        self.requests_per_second = requests_per_second
        self.request_times = []
        self.last_request_time = 0

    def wait_if_needed(self):
        current_time = time.time()
        time_since_last = current_time - self.last_request_time
        if time_since_last < (1 / self.requests_per_second):
            time.sleep((1 / self.requests_per_second) - time_since_last)
        current_time = time.time()
        self.request_times = [t for t in self.request_times if current_time - t < 60]
        if len(self.request_times) >= self.requests_per_minute:
            time.sleep(60 - (current_time - self.request_times[0]))
        self.request_times.append(current_time)
        self.last_request_time = current_time

rate_limiter = RateLimiter()

def get_embedding(text: str, max_retries: int = 3) -> list[float]:
    for attempt in range(max_retries):
        try:
            rate_limiter.wait_if_needed()
            input_obj = TextEmbeddingInput(text=text, task_type=TASK_TYPE)
            response = embedding_model.get_embeddings([input_obj])
            return response[0].values
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)

# --- Chunking Functions ---
def extract_topic_chunk(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    posts = re.split(r"^---\s*$", content, flags=re.MULTILINE)
    urls = []
    for post in posts:
        match = re.search(r"\*\*URL:\*\*\s*(https?://[^\s]+)", post)
        if match:
            urls.append(match.group(1))

    url_refs = "\n".join(f"- {url}" for url in urls)
    chunk_text = f"[SOURCE LINKS]\n{url_refs}\n\n{content.strip()}"
    return (chunk_text, urls)

def extract_tool_chunk(file_path: Path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
    if not content:
        return None
    name = file_path.stem
    url = f"https://tds.s-anand.net/#/{name}"
    chunk_text = f"[SOURCE: {url}]\n\n{content}"
    return (chunk_text, [url])

# --- Retry mechanism ---
FAILURE_LOG_PATH = "embedding_output/failures.log"

def log_failure(file_path, label, reason):
    with open(FAILURE_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps({"file": str(file_path), "label": label, "reason": reason}) + "\n")

def load_failures():
    if not os.path.exists(FAILURE_LOG_PATH):
        return []
    with open(FAILURE_LOG_PATH, "r", encoding="utf-8") as f:
        return [json.loads(line.strip()) for line in f if line.strip()]

def save_final_output(data):
    os.makedirs("embedding_output", exist_ok=True)
    np.savez_compressed("embedding_output/final_embeddings.npz",
                        embeddings=np.array([d["embedding"] for d in data]),
                        chunks=np.array([d["text"] for d in data]))
    with open("embedding_output/metadata.json", "w", encoding="utf-8") as f:
        json.dump([{k: v for k, v in d.items() if k != "embedding"} for d in data], f, indent=2)

# --- Main process ---
def process_markdowns():
    TOPICS_DIR = Path("markdowns/topics_markdown")
    TOOLS_DIR = Path("markdowns/tools-in-data-science-public")
    topic_files = list(TOPICS_DIR.rglob("*.md"))
    tool_files = list(TOOLS_DIR.rglob("*.md"))
    all_data = []

    print("📘 Processing topic markdowns...")
    for file in tqdm(topic_files):
        try:
            result = extract_topic_chunk(file)
            if not result:
                continue
            text, urls = result
            embedding = get_embedding(text)
            all_data.append({
                "text": text,
                "embedding": embedding,
                "url": urls,
                "label": "topic"
            })
        except Exception as e:
            log_failure(file, "topic", str(e))

    print("🔧 Processing tool markdowns...")
    for file in tqdm(tool_files):
        try:
            result = extract_tool_chunk(file)
            if not result:
                continue
            text, urls = result
            embedding = get_embedding(text)
            all_data.append({
                "text": text,
                "embedding": embedding,
                "url": urls,
                "label": "tool"
            })
        except Exception as e:
            log_failure(file, "tool", str(e))

    return all_data

def retry_failures(data, max_retries=10):
    for attempt in range(max_retries):
        failures = load_failures()
        if not failures:
            break
        print(f"🔁 Retry Attempt {attempt+1} with {len(failures)} failures...")
        os.remove(FAILURE_LOG_PATH)
        for entry in tqdm(failures):
            try:
                file = Path(entry["file"])
                label = entry["label"]
                if label == "topic":
                    result = extract_topic_chunk(file)
                else:
                    result = extract_tool_chunk(file)
                if not result:
                    continue
                text, urls = result
                embedding = get_embedding(text)
                data.append({
                    "text": text,
                    "embedding": embedding,
                    "url": urls,
                    "label": label
                })
            except Exception as e:
                log_failure(file, label, str(e))

    # Final status
    final_failures = load_failures()
    if final_failures:
        print(f"⚠️ {len(final_failures)} files still failed after retries. See {FAILURE_LOG_PATH}")
    else:
        print("✅ All chunks successfully embedded after retries.")

    return data

if __name__ == "__main__":
    all_data = process_markdowns()
    all_data = retry_failures(all_data, max_retries=10)
    save_final_output(all_data)
    print(f"\n🎉 Completed! Saved {len(all_data)} chunks.")
