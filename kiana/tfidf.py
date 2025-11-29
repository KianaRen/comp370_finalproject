import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS

CANADIAN_POLITICS = "/Users/kiana/Desktop/comp370/comp370_finalproject/data/category/Canadian_Politics.csv"
INTERNATIONAL_POLITICS = "/Users/kiana/Desktop/comp370/comp370_finalproject/data/category/International_Politics.csv"
PERSONAL_LIFE = "/Users/kiana/Desktop/comp370/comp370_finalproject/data/category/Personal_Life.csv"
RESIGNATION = "/Users/kiana/Desktop/comp370/comp370_finalproject/data/category/Resignation.csv"
US_RELATIONS = "/Users/kiana/Desktop/comp370/comp370_finalproject/data/category/US_Relations.csv"

FILE_NAMES = [
    CANADIAN_POLITICS, 
    INTERNATIONAL_POLITICS, 
    PERSONAL_LIFE, 
    RESIGNATION, 
    US_RELATIONS
]
TOP_N_WORDS = 10


all_texts = []
category_dfs = {}

for file_name in FILE_NAMES:
    df = pd.read_csv(file_name)
        
    df['text'] = df['title'].fillna('') + ' ' + df['description'].fillna('')
    
    category_dfs[file_name] = df
    all_texts.extend(df['text'].tolist())


custom_stop_words = set(['justin', 'trudeau', 'canada', 'prime', 'minister'])
full_stop_words = list(ENGLISH_STOP_WORDS.union(custom_stop_words))
vectorizer = TfidfVectorizer(
    stop_words=full_stop_words, 
    token_pattern=r'\b[a-z]{3,}\b', 
    lowercase=True
)


vectorizer.fit(all_texts)
feature_names = vectorizer.get_feature_names_out()



print("\n" + "=" * 60)

for file_name, df in category_dfs.items():
    category_name = file_name.removeprefix("/Users/kiana/Desktop/comp370/comp370_finalproject/data/category/").replace('.csv', '').replace('_', ' ')
    
    # 1. Transform the documents of the current category using the Global IDF
    tfidf_matrix = vectorizer.transform(df['text'])
    
    # 2. Calculate the overall importance of each word (aggregate score)
    word_importance = tfidf_matrix.sum(axis=0).A1 
    
    # 3. Create a Series for easy sorting and ranking
    scores_series = pd.Series(word_importance, index=feature_names)
    top_words = scores_series.nlargest(TOP_N_WORDS)
    
    # 4. Print the results
    print(f"\nCATEGORY: {category_name}")
    print("-" * 42)
    print(f"{'Word':<20} {'ti-idf score':>20}")
    print("-" * 42)
    for word, score in top_words.items():
        print(f"{word:<20} {score:20.4f}")
        
print("=" * 60)