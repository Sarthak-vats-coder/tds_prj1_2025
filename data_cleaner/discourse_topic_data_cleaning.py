import json
from datetime import datetime

# Load the JSON data
with open('discourse_all_topics.json', 'r') as f:
    data = json.load(f)

# Define the date cutoff: 31st Dec 2024
cutoff = datetime.strptime('2024-12-31T23:59:59', '%Y-%m-%dT%H:%M:%S')

# Filter and extract required fields
filtered = []
for item in data:
    created_at = datetime.strptime(item["created_at"], '%Y-%m-%dT%H:%M:%S.%fZ')
    if created_at > cutoff:
        filtered.append({
            "id": item["id"],
            "title": item["title"],
            "slug": item.get("slug"),
            "posts_count": item["posts_count"],
            "reply_count": item["reply_count"],
            "created_at": item["created_at"],
            "last_posted_at": item["last_posted_at"],
            "tags": item.get("tags", []),
            "featured_link": item.get("featured_link")
        })

# Save the cleaned data
with open('cleaned_topics.json', 'w') as f:
    json.dump(filtered, f, indent=4)
