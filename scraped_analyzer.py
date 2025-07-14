# scraped_analyzer.py

from textblob import TextBlob
from collections import Counter
import re

def analyze_scraped_data(user_data):
    all_texts = []

    for p in user_data.get("posts", []):
        all_texts.append(p["title"] + " " + p["selftext"])

    for c in user_data.get("comments", []):
        all_texts.append(c["body"])

    full_text = " ".join(all_texts).lower()
    words = re.findall(r'\b[a-z]{4,}\b', full_text)
    top_keywords = Counter(words).most_common(10)

    top_subreddits = Counter(
        [p['subreddit'] for p in user_data.get("posts", [])] +
        [c['subreddit'] for c in user_data.get("comments", [])]
    ).most_common(5)

    sentiment_scores = [TextBlob(text).sentiment.polarity for text in all_texts if len(text) > 20]
    avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0

    tone = (
        "Positive & Optimistic" if avg_sentiment > 0.2 else
        "Neutral/Reserved" if -0.2 <= avg_sentiment <= 0.2 else
        "Negative or Cynical"
    )

    return {
        "top_keywords": top_keywords,
        "top_subreddits": top_subreddits,
        "total_posts": len(user_data.get("posts", [])),
        "total_comments": len(user_data.get("comments", [])),
        "emotional_tone": tone,
        "avg_sentiment": round(avg_sentiment, 3),
    }
