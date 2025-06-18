import json
import os
import re
import requests
import time
from tqdm import tqdm
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def sanitize_filename(name):
    return re.sub(r'[\\/:"*?<>|]+', '', name).strip().replace(' ', '_')[:80]

CACHE_PATH = "image_description_cache.json"
if os.path.exists(CACHE_PATH):
    with open(CACHE_PATH, 'r') as f:
        image_description_cache = json.load(f)
else:
    image_description_cache = {}

def generate_image_description(image_url):
    image_url = image_url.replace("\\", "")

    if image_url in image_description_cache:
        return image_description_cache[image_url]

    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not set in environment.")
    genai.configure(api_key=api_key)

    try:
        image_bytes = requests.get(image_url).content
    except Exception:
        return "Image unavailable"

    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        response = model.generate_content([
            "Describe this image in one sentence:",
            {"mime_type": "image/jpeg", "data": image_bytes}
        ])
        description = response.text if hasattr(response, 'text') else str(response)
    except Exception:
        description = "Image description failed"

    image_description_cache[image_url] = description
    with open(CACHE_PATH, 'w') as f:
        json.dump(image_description_cache, f, indent=2)

    time.sleep(4.5)
    return description

def html_to_markdown_with_image_descriptions(html):
    soup = BeautifulSoup(html, 'html.parser')

    for img in soup.find_all('img'):
        src = img.get('src', '').replace("\\", "")
        if src:
            alt_text = generate_image_description(src)
            img.replace_with(f"![{alt_text}]({src})")

    for a in soup.find_all('a'):
        href = a.get('href', '')
        text = a.text.strip()
        a.replace_with(f"[{text}]({href})")

    for code in soup.find_all(['code', 'pre']):
        code.replace_with(f"`{code.text.strip()}`")

    for tag in soup.find_all(['p', 'br']):
        tag.insert_after('\n\n')

    return soup.get_text().strip()

# Load JSON
with open('cleaned_posts.json', 'r') as f:
    data = json.load(f)

output_dir = "topics_markdown"
os.makedirs(output_dir, exist_ok=True)

print("🚀 Processing topics...")
for i, (topic_id, topic_info) in enumerate(tqdm(data.items(), desc="Topics")):
    title = topic_info.get("title", f"topic_{topic_id}")
    filename = sanitize_filename(title) or f"topic_{topic_id}"
    filepath = os.path.join(output_dir, f"{filename}.md")

    md_content = f"# {title}\n"
    md_content += f"_Slug: {topic_info.get('slug', '')}_\n\n"

    for post in topic_info['posts']:
        post_id = post.get('id')
        post_url = post.get('post_url', '').strip()
        full_url = f"https://discourse.onlinedegree.iitm.ac.in{post_url}" if post_url.startswith("/t/") else "N/A"

        md_content += f"---\n"
        md_content += f"**Post ID:** {post_id}  \n"
        md_content += f"**URL:** {full_url}  \n\n"
        md_content += html_to_markdown_with_image_descriptions(post['cooked']) + "\n\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md_content)

print(f"✅ All markdown files saved in `{output_dir}` with full discourse post URLs.")
