import pandas as pd
import re

# Define file paths
raw_path = 'C:/Users/hp/Desktop/10 Acadamy/VS code/fintech-app-review-analysis/Data/raw_reviews.csv'
processed_path = 'C:/Users/hp/Desktop/10 Acadamy/VS code/fintech-app-review-analysis/Data/processed_reviews.csv'

# Load raw data
df = pd.read_csv(raw_path)

# Drop duplicates and rows where the review column is NaN
df.drop_duplicates(inplace=True)
df.dropna(subset=['review'], inplace=True)

# Clean the review text function
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    return text

# Apply cleaning function to the 'review' column and save as 'clean_text'
df['clean_text'] = df['review'].apply(clean_text)

# Save the processed dataframe
df.to_csv(processed_path, index=False)
print(f"✅ Saved cleaned reviews to {processed_path}")
