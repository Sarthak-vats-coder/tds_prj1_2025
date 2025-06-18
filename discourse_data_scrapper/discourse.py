import requests
import json
import time
from datetime import datetime

# Load cookie
with open("cookie.txt", "r") as file:
    cookies = file.read().strip()

headers = {
    "Cookie": cookies
}

base_url = "https://discourse.onlinedegree.iitm.ac.in/c/courses/tds-kb/34.json?page="
all_topics = []
filtered_topics = []
page = 1

# Set the cutoff datetime: 15 April 2025 (UTC assumed)
cutoff_date = datetime.strptime("2025-04-15T23:59:59", "%Y-%m-%dT%H:%M:%S")

while True:
    print(f"Fetching page {page}...")
    url = base_url + str(page)
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch page {page}, status code: {response.status_code}")
        break

    data = response.json()
    topics = data.get("topic_list", {}).get("topics", [])

    if not topics:
        print("No more topics found.")
        break

    for topic in topics:
        created_at = topic.get("created_at", "")
        tags = topic.get("tags", [])

        try:
            created_datetime = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            continue  # Skip malformed dates

        if created_datetime <= cutoff_date and "term1-2025" in tags:
            filtered_topics.append(topic)

    all_topics.extend(topics)
    page += 1
    time.sleep(1)

# Save raw and filtered data
with open("discourse_all_topics.json", "w") as f:
    json.dump(all_topics, f, indent=4)

with open("discourse_jan2025_topics.json", "w") as f:
    json.dump(filtered_topics, f, indent=4)

print(f"Total topics fetched: {len(all_topics)}")
print(f"Total Jan 2025 topics (before 15 Apr 2025): {len(filtered_topics)}")
