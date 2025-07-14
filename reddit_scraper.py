# reddit_scraper.py

import praw
import os
from dotenv import load_dotenv

load_dotenv()

REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = "RedditPersonaScraper/0.1"

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT
)

def scrape_user_data(username, max_items=100):
    try:
        redditor = reddit.redditor(username)

        user_data = {
            "username": username,
            "posts": [],
            "comments": []
        }

        # Scrape posts
        for submission in redditor.submissions.new(limit=max_items):
            user_data["posts"].append({
                "title": submission.title,
                "selftext": submission.selftext,
                "subreddit": str(submission.subreddit),
                "url": submission.url
            })

        # Scrape comments
        for comment in redditor.comments.new(limit=max_items):
            user_data["comments"].append({
                "body": comment.body,
                "subreddit": str(comment.subreddit),
                "link": f"https://www.reddit.com{comment.permalink}"
            })

        return user_data

    except Exception as e:
        print(f"Error scraping u/{username}: {e}")
        return None
