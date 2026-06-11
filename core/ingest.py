import json
import requests

def load_sample_data(path="data/sample_posts.json"):
    with open(path, "r") as f:
        return json.load(f)


def fetch_reddit_mock():
    """
    Simple fallback mock fetch.
    You can replace this with Reddit API later.
    """
    return [
        "AI is changing the world بسرعة",
        "Python is amazing for data science",
        "Stock market is very volatile today",
        "OpenAI releases new model and it's powerful",
        "Cybersecurity threats are increasing"
    ]
