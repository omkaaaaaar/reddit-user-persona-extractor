import praw

# Hardcoded credentials (make sure they're valid)
CLIENT_ID = "yrB1R0tjF6iHWsTpz_WTMg"
CLIENT_SECRET = "pzd9TVQi_PXuKkHze_yp1aIT9g6jmA"
USER_AGENT = "mac:reddit-user-persona-extractor:v1.0 (by /u/diligent-recover-238)"

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
                "selftext": submission.selftext,
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
