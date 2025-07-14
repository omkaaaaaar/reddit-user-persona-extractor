import praw
import os
from dotenv import load_dotenv

# Load Reddit API credentials from .env
load_dotenv()

CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
USER_AGENT = os.getenv("REDDIT_USER_AGENT")

if not all([CLIENT_ID, CLIENT_SECRET, USER_AGENT]):
    print("⚠️ Warning: Missing Reddit API credentials. Create a .env file with keys.")

def scrape_user_data(username, post_limit=30, comment_limit=30):
    try:
        reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT
        )

        user = reddit.redditor(username)

        posts = []
        comments = []

        for submission in user.submissions.new(limit=post_limit):
            posts.append({
                "title": submission.title,
                "selftext": submission.selftext or "",
                "subreddit": submission.subreddit.display_name,
                "url": submission.url
            })

        for comment in user.comments.new(limit=comment_limit):
            comments.append({
                "body": comment.body,
                "subreddit": comment.subreddit.display_name,
                "link": f"https://reddit.com{comment.permalink}"
            })

        return {"posts": posts, "comments": comments}

    except Exception as e:
        print(f"❌ Error scraping Reddit: {e}")
        return {"posts": [], "comments": []}
