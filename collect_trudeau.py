import requests
import json
import time

API_TOKEN = "p5m5gFYnYMWrqSEd5WPWTk8CGcV78OBYfRa6JPMX"
SEARCH_TERM = "Trudeau"
LIMIT = 3                    # API restriction
TARGET_ARTICLE_COUNT = 600   # your goal
BASE_URL = "https://api.thenewsapi.com/v1/news/all"

all_articles = []
page = 1 
# Antoine = pages 1-60
# Kiana = pages 61-120
# Zahra = pages 121-180

while len(all_articles) < TARGET_ARTICLE_COUNT:
    url = f"{BASE_URL}?api_token={API_TOKEN}&language=en&limit={LIMIT}&search=%22{SEARCH_TERM}%22&page={page}"

    print(f"Pulling page {page} ...")
    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        break

    data = response.json()
    articles = data.get("data", [])

    if not articles:
        print("No more articles returned by API. Stopping.")
        break

    all_articles.extend(articles)

    print(f"Total collected so far: {len(all_articles)}")
    page += 1

    time.sleep(0.5)  # avoid hammering the API

# Trim in case we exceed 600
all_articles = all_articles[:TARGET_ARTICLE_COUNT]

# ----- SAVE TO JSON -----

output_filename = "trudeau_articles.json"

with open(output_filename, "w", encoding="utf-8") as f:
    json.dump(all_articles, f, indent=4, ensure_ascii=False)

print(f"\nFinished! Saved {len(all_articles)} articles to {output_filename}")
