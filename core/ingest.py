import praw

# You will fill these in
REDDIT_CLIENT_ID = "your_client_id"
REDDIT_CLIENT_SECRET = "your_client_secret"
REDDIT_USER_AGENT = "social-intelligence-engine by vic"


def fetch_reddit_posts(subreddit_name="technology", limit=20):
    """
    Fetch real posts from Reddit using PRAW
    """

    reddit = praw.Reddit(
        client_id=REDDIT_CLIENT_ID,
        client_secret=REDDIT_CLIENT_SECRET,
        user_agent=REDDIT_USER_AGENT
    )

    subreddit = reddit.subreddit(subreddit_name)

    posts = []

    for post in subreddit.hot(limit=limit):
        text = f"{post.title} {post.selftext}".strip()
        if text:
            posts.append(text)

    return posts
