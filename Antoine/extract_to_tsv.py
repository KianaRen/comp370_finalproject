import json
import csv

def find_article_list(data):
    # If it's already a list of articles
    if isinstance(data, list):
        return data

    # Common container keys that may hold a list of articles
    if isinstance(data, dict):
        for key in ("articles", "data", "items", "results"):
            val = data.get(key)
            if isinstance(val, list):
                return val

        # If dict values are lists, return the first list found
        for val in data.values():
            if isinstance(val, list):
                return val

    return []


def extract_fields(item):
    # Safe accessor for likely field names
    title = (
        item.get("title")
        or item.get("headline")
        or item.get("name")
        or ""
    )

    description = (
        item.get("description")
        or item.get("summary")
        or item.get("lead")
        or item.get("lead_paragraph")
        or ""
    )

    snippet = (
        item.get("snippet")
        or item.get("excerpt")
        or item.get("content")
        or item.get("body")
        or ""
    )

    if not snippet and description:
        snippet = description[:200]

    # Ensure strings (avoid None)
    return str(title), str(description), str(snippet)


def load_posts(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    articles = find_article_list(data)

    # If nothing recognizable found, and top-level is a dict of dicts, try collecting dict values
    if not articles and isinstance(data, dict):
        candidates = [v for v in data.values() if isinstance(v, dict)]
        if candidates:
            articles = candidates

    extracted = []
    for item in articles:
        if not isinstance(item, dict):
            continue
        title, description, snippet = extract_fields(item)
        if title or description or snippet:
            extracted.append((title, description, snippet))

    return extracted


def main():
    
    selected_posts = load_posts("trudeau_articles_page1-34.json")
    
    with open("articles_trudeau.tsv", "w", encoding="utf-8", newline="") as f:
        tsv_writer = csv.writer(f, delimiter="\t")
        tsv_writer.writerow(["title", "description", "snippet"])  # Header
        for title, description, snippet in selected_posts:
            tsv_writer.writerow([title, description, snippet])

    print(f"Extracted {len(selected_posts)} articles to articles_trudeau.tsv")

if __name__ == "__main__":
    main()
