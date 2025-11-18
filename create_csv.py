import json
import csv
import glob

# Folder containing your JSON files (change this!)
INPUT_FOLDER = "data/*.json"
OUTPUT_CSV = "articles.csv"

def main():
    # Find all JSON files in the folder
    json_files = glob.glob(INPUT_FOLDER)

    rows = []

    for file in json_files:
        with open(file, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                print(f"Skipping {file}: JSON decode error")
                continue

        # Each file contains a list of objects
        for item in data:
            title = item.get("title", "")
            description = item.get("description", "")

            rows.append([title, description])

    # Write to CSV
    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["title", "description"])  # header
        writer.writerows(rows)

    print(f"Done! Extracted {len(rows)} articles into {OUTPUT_CSV}")

if __name__ == "__main__":
    main()

