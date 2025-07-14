from textblob import TextBlob
from collections import Counter
import re

def clean_text(text):
    return re.sub(r"[^\w\s]", "", text.lower())

def analyze_scraped_data(data):
    sentiments, all_words, subreddits = [], [], []

    for post in data.get("posts", []):
        text = f"{post['title']} {post['selftext']}"
        sentiments.append(TextBlob(text).sentiment.polarity)
        all_words += clean_text(text).split()
        subreddits.append(post['subreddit'])

    for comment in data.get("comments", []):
        text = comment['body']
        sentiments.append(TextBlob(text).sentiment.polarity)
        all_words += clean_text(text).split()
        subreddits.append(comment['subreddit'])

    avg_sentiment = round(sum(sentiments) / len(sentiments), 3) if sentiments else 0
    tone = "Positive" if avg_sentiment > 0.2 else "Negative" if avg_sentiment < -0.2 else "Neutral/Reserved"

    top_subreddits = Counter(subreddits).most_common(5)
    top_keywords = Counter(all_words).most_common(10)

    return {
        "avg_sentiment": avg_sentiment,
        "emotional_tone": tone,
        "top_subreddits": top_subreddits,
        "top_keywords": top_keywords
    }
