import praw

# ✅ REPLACE these values with your actual Reddit App credentials
reddit = praw.Reddit(
    client_id="yrB1R0tjF6iHWsTpz_WTMg",
    client_secret="pzd9TVQi_PXuKkHze_yp1aIT9g6jmA",
    user_agent="mac:reddit-user-persona-extractor:v1.0 (by /u/Diligent-Recover-238)"
)

def scrape_user_data(username):
    posts = []
    comments = []

    try:
        redditor = reddit.redditor(username)

        for post in redditor.submissions.new(limit=20):
            posts.append({
                "title": post.title,
                "selftext": post.selftext,
                "subreddit": str(post.subreddit),
                "link": f"https://www.reddit.com{post.permalink}"
            })

        for comment in redditor.comments.new(limit=30):
            comments.append({
                "body": comment.body,
                "subreddit": str(comment.subreddit),
                "link": f"https://www.reddit.com{comment.permalink}"
            })

    except Exception as e:
        print(f"❌ Error scraping Reddit: {e}")

    return {"posts": posts, "comments": comments}
