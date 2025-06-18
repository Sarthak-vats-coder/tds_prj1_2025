import requests
import json
import time
import os
from tqdm import tqdm

# Load cookie
with open("cookie.txt", "r") as file:
    cookies = file.read().strip()

headers = {
    "Cookie": cookies,
    "User-Agent": "Mozilla/5.0"
}

# Input/output paths
INPUT_FILE = "cleaned_topics.json"
OUTPUT_FILE = "discourse_jan2025_all_posts.json"
LOG_FILE = "log.txt"

# Load input topics
with open(INPUT_FILE, "r") as file:
    topics = json.load(file)

# Load existing results if any (resume feature)
if os.path.exists(OUTPUT_FILE):
    with open(OUTPUT_FILE, "r") as f:
        all_topic_data = json.load(f)
else:
    all_topic_data = {}

# Logger
def log(msg):
    print(msg)
    with open(LOG_FILE, "a") as logf:
        logf.write(msg + "\n")

# Chunking helper
def chunked(iterable, size):
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

# Loop through all topics
for topic in tqdm(topics, desc="Scraping topics", unit="topic"):
    topic_id = str(topic["id"])

    # Skip if already done
    if topic_id in all_topic_data:
        continue

    topic_title = topic["title"]
    topic_slug = topic["slug"]
    log(f"\n📘 Fetching topic {topic_id}: {topic_title}")

    try:
        # Step 1: Initial request
        url = f"https://discourse.onlinedegree.iitm.ac.in/t/{topic_id}.json?track_visit=true&forceLoad=true"
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            log(f"❌ Failed initial fetch for {topic_id}, status: {response.status_code}")
            continue

        topic_data = response.json()
        initial_posts = topic_data.get("post_stream", {}).get("posts", [])
        full_stream = topic_data.get("post_stream", {}).get("stream", [])
        all_posts = initial_posts[:]
        fetched_ids = {post["id"] for post in initial_posts}
        remaining_ids = [pid for pid in full_stream if pid not in fetched_ids]

        log(f"🔍 Got {len(initial_posts)} initial posts, {len(remaining_ids)} remaining...")

        # Step 2: Fetch remaining post IDs
        for batch in chunked(remaining_ids, 20):
            post_ids_str = "&".join([f"post_ids[]={pid}" for pid in batch])
            paginated_url = f"https://discourse.onlinedegree.iitm.ac.in/t/{topic_id}/posts.json?{post_ids_str}&include_suggested=true"

            retry_count = 0
            while retry_count < 3:
                paginated_response = requests.get(paginated_url, headers=headers)
                if paginated_response.status_code == 200:
                    posts_data = paginated_response.json().get("post_stream", {}).get("posts", [])
                    all_posts.extend(posts_data)
                    break
                else:
                    retry_count += 1
                    log(f"⚠️ Retry {retry_count} for batch: {batch[0]}–{batch[-1]}")
                    time.sleep(2)

            if retry_count == 3:
                log(f"❌ Failed to fetch batch: {batch}")
            time.sleep(1)

        # Store final topic data
        all_topic_data[topic_id] = {
            "title": topic_title,
            "slug": topic_slug,
            "posts": all_posts
        }

        # Save progress after every topic
        with open(OUTPUT_FILE, "w") as f:
            json.dump(all_topic_data, f, indent=2)

    except Exception as e:
        log(f"⚠️ Error in topic {topic_id}: {str(e)}")
        continue

log(f"\n✅ All done. Total topics saved: {len(all_topic_data)}")
