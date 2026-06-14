import re
from collections import Counter


def clean_text(text):
    text = text.lower()

    text = re.sub(
        r"[^a-zA-Z0-9\s]",
        "",
        text
    )

    return text


def extract_keywords(posts):

    all_words = []

    stopwords = {
        "the",
        "is",
        "and",
        "to",
        "of",
        "a",
        "in",
        "for",
        "on",
        "with",
        "that",
        "this",
        "are",
        "was",
        "were",
        "be"
    }

    for post in posts:

        words = clean_text(post).split()

        filtered = [
            word
            for word in words
            if word not in stopwords
            and len(word) > 2
        ]

        all_words.extend(filtered)

    return Counter(all_words)
