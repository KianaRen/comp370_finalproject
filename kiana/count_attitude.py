import pandas as pd
import sys

def analyze_attitudes(file_path):

    df = pd.read_csv(file_path)
    attitude_col = 'attitude'

    df[attitude_col] = df[attitude_col].str.lower().str.strip()
    counts = df[attitude_col].value_counts()
    
    count_pos = counts.get('positive', 0)
    count_neg = counts.get('negative', 0)
    count_neu = counts.get('neutral', 0)
    
    total_entries = count_pos + count_neg + count_neu

    def get_percentage(count, total):
        return (count / total) * 100 if total > 0 else 0
        
    perc_pos = get_percentage(count_pos, total_entries)
    perc_neg = get_percentage(count_neg, total_entries)
    perc_neu = get_percentage(count_neu, total_entries)

    # 4. Print the results in the specified format
    print(f"\n{file_path}")
    print(f"Total entries: {total_entries}")
    print(f"Positive: {perc_pos:.2f}% ({count_pos})")
    print(f"Negative: {perc_neg:.2f}% ({count_neg})")
    print(f"Neutral: {perc_neu:.2f}% ({count_neu})")
    print("-" * 40)

CANADIAN_POLITICS = "/Users/kiana/Desktop/comp370/comp370_finalproject/data/category/Canadian_Politics.csv"
INTERNATIONAL_POLITICS = "/Users/kiana/Desktop/comp370/comp370_finalproject/data/category/International_Politics.csv"
PERSONAL_LIFE = "/Users/kiana/Desktop/comp370/comp370_finalproject/data/category/Personal_Life.csv"
RESIGNATION = "/Users/kiana/Desktop/comp370/comp370_finalproject/data/category/Resignation.csv"
US_RELATIONS = "/Users/kiana/Desktop/comp370/comp370_finalproject/data/category/US_Relations.csv"

INPUT_FILE = US_RELATIONS 

# Call the function
analyze_attitudes(INPUT_FILE)