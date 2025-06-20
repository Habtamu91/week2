import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

def plot_sentiment_distribution(df, sentiment_col='sentiment'):
    plt.figure(figsize=(8,6))
    sns.countplot(data=df, x=sentiment_col, order=df[sentiment_col].value_counts().index)
    plt.title('Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.show()

def plot_topic_distribution(df, topic_col='dominant_topic'):
    plt.figure(figsize=(8,6))
    sns.countplot(data=df, x=topic_col, order=sorted(df[topic_col].unique()))
    plt.title('Topic Distribution')
    plt.xlabel('Topic')
    plt.ylabel('Number of Reviews')
    plt.tight_layout()
    plt.show()

def generate_wordcloud(words, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(words)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    plt.show()

def main():
    # Load the data with sentiment labels
<<<<<<< HEAD
    df = pd.read_csv('C:/Users/hp/Desktop/10 Acadamy/VS code/fin/fintech-app-review-analysis/Data/processed_reviews.csv')
=======
    df = pd.read_csv('C:/Users/hp/Desktop/10 Acadamy/VS code/fintech-app-review-analysis/Data/processed_reviews.csv')
>>>>>>> task-2

    # Plot sentiment distribution
    if 'sentiment' in df.columns:
        plot_sentiment_distribution(df)
    else:
        print("No 'sentiment' column found in the data.")

    # If you have dominant topic info (e.g., from thematic analysis saved back), plot topic distribution
    if 'dominant_topic' in df.columns:
        plot_topic_distribution(df)
    else:
        print("No 'dominant_topic' column found in the data.")

    # Example: Wordclouds for topics (if you have topic keywords stored)
    # You can prepare a dictionary of topic_id: keywords_string and visualize:
    topic_keywords = {
        1: "loan interest rate repayment credit",
        2: "service staff branch support",
        3: "mobile app easy access",
        4: "customer complaint delay response",
        5: "ATM cash withdrawal deposit"
    }

    for topic_id, keywords in topic_keywords.items():
        generate_wordcloud(keywords, title=f"Topic {topic_id} Word Cloud")

if __name__ == "__main__":
    main()
