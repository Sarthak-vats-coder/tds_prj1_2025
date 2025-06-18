import json

# Load input JSON file
with open('discourse_jan2025_all_posts.json', 'r') as f:
    data = json.load(f)

# Filter out unnecessary fields
cleaned_data = {}
for topic_id, topic_info in data.items():
    cleaned_posts = []
    for post in topic_info.get("posts", []):
        cleaned_posts.append({
            "id": post["id"],
            "cooked": post["cooked"],
            "post_url": post.get("post_url")
        })
    
    cleaned_data[topic_id] = {
        "title": topic_info.get("title"),
        "posts": cleaned_posts
    }

# Save cleaned output
with open('cleaned_posts.json', 'w') as f:
    json.dump(cleaned_data, f, indent=4)
