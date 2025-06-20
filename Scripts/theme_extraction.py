import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import argparse

def load_data(filepath):
    """Load preprocessed reviews CSV file."""
<<<<<<< HEAD
    df = pd.read_csv('C:/Users/hp/Desktop/10 Acadamy/VS code/fin/fintech-app-review-analysis/Data/processed_reviews.csv')
=======
    df = pd.read_csv('C:/Users/hp/Desktop/10 Acadamy/VS code/fintech-app-review-analysis/Data/processed_reviews.csv')
>>>>>>> task-2
    return df

def preprocess_text_column(df, text_col='clean_text'):
    """Ensure text column is string and non-empty."""
    df[text_col] = df[text_col].fillna('').astype(str)
    return df

def vectorize_text(texts, max_df=0.95, min_df=2, stop_words='english'):
    """Convert text to document-term matrix."""
    vectorizer = CountVectorizer(max_df=max_df, min_df=min_df, stop_words=stop_words)
    dtm = vectorizer.fit_transform(texts)
    return dtm, vectorizer

def fit_lda(dtm, n_topics=5, random_state=42):
    """Fit Latent Dirichlet Allocation model."""
    lda = LatentDirichletAllocation(n_components=n_topics, random_state=random_state)
    lda.fit(dtm)
    return lda

def display_topics(model, feature_names, no_top_words=10):
    """Print top words for each topic."""
    for topic_idx, topic in enumerate(model.components_):
        print(f"\nTopic {topic_idx + 1}:")
        print(", ".join([feature_names[i] for i in topic.argsort()[:-no_top_words - 1:-1]]))

def main(data_path, n_topics):
    print("Loading data...")
    df = load_data(data_path)
    df = preprocess_text_column(df)

    print("Vectorizing text...")
    dtm, vectorizer = vectorize_text(df['clean_text'])

    print(f"Fitting LDA with {n_topics} topics...")
    lda = fit_lda(dtm, n_topics=n_topics)

    print("Top words per topic:")
    display_topics(lda, vectorizer.get_feature_names_out())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform Thematic Analysis (Topic Modeling) on Bank Reviews.")
    parser.add_argument("--data_path", type=str, default="../data/processed_reviews.csv",
                        help="Path to preprocessed reviews CSV")
    parser.add_argument("--n_topics", type=int, default=5, help="Number of topics to extract")
    args = parser.parse_args()

    main(args.data_path, args.n_topics)
<<<<<<< HEAD
=======

>>>>>>> task-2
