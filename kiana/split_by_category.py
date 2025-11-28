import pandas as pd


input_file_name = "/Users/kiana/Desktop/comp370/comp370_finalproject/data/annotated/all.csv"
df = pd.read_csv(input_file_name)


output_cols = ['attitude', 'title', 'description']

categories_in_data = df['category'].unique()

print(f"Found {len(categories_in_data)} unique categories. Creating separate files...")

# Loop through the unique categories and create a new file for each
for category in categories_in_data:
    # Handle missing category values if they exist, to prevent errors
    if pd.isna(category):
        filename = "No_Category.csv"
        category_df = df[df['category'].isna()]
    else:
        # Filter the DataFrame for the current category
        category_df = df[df['category'] == category]
        filename = f"{str(category).replace(' ', '_')}.csv"

    # Select only the required columns
    output_df = category_df[output_cols]

    # Save the filtered DataFrame to a new CSV file without the index
    output_df.to_csv(filename, index=False)
    
    print(f"Successfully created file: {filename}")