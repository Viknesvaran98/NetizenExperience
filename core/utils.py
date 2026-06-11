import re
from collections import Counter

def clean_text(text: str):
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text


def extract_keywords(posts):
    words = []

    for p in posts:
        clean = clean_text(p)
        words.extend(clean.split())

    stopwords = set([
        "the", "is", "and", "to", "a", "of", "in", "it", "this", "that",
        "for", "on", "with", "as", "was", "are", "at"
    ])

    filtered = [w for w in words if w not in stopwords and len(w) > 2]

    return Counter(filtered)
