from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def get_sentiment(text: str):
    """
    Analyze sentiment of a text string.

    Returns:
    {
        "label": "positive",
        "score": 0.85
    }
    """

    scores = analyzer.polarity_scores(text)

    compound = scores["compound"]

    if compound >= 0.05:
        label = "positive"
    elif compound <= -0.05:
        label = "negative"
    else:
        label = "neutral"

    return {
        "label": label,
        "score": round(compound, 4)
    }


def batch_sentiment(posts):
    """
    Analyze multiple posts.
    """

    results = []

    for post in posts:
        results.append(
            {
                "text": post,
                "analysis": get_sentiment(post)
            }
        )

    return results
