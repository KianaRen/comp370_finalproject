import requests
import time
import json

API_TOKEN = "xeuLSxZsvD0R1l1qGKhjwfKZCck0pkQkWFKW2fVI"
SEARCH_TERM = "Trudeau"
LIMIT = 3
TARGET_ARTICLE_COUNT = 100
LOCALE = "us,ca"
PUBLISHED_AFTER = "2024-11-14"
SORT = "relevance_score"
BASE_URL = "https://api.thenewsapi.com/v1/news/all"

all_articles = []
page = 121
#Antoine: 1-60
#Kiana: 61-120
#Zahra: 121-180

while len(all_articles) < TARGET_ARTICLE_COUNT:
    params = {
        "api_token": API_TOKEN,
        "language": "en",
        "limit": LIMIT,
        "search": SEARCH_TERM,
        "page": page,
        "locale": LOCALE,
        "published_after": PUBLISHED_AFTER,
        "sort": SORT,
    }

    print(f"Pulling page {page} ...")
    response = requests.get(BASE_URL, params=params)

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
    time.sleep(0.5)

all_articles = all_articles[:TARGET_ARTICLE_COUNT]

with open("zahra_trudeau_articles.json", "w", encoding="utf-8") as f:
    json.dump(all_articles, f, indent=4)

print(f"\nFinished! Saved {len(all_articles)} articles to zahra_trudeau_articles.json")

