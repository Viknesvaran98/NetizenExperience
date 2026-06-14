from core.sentiment import get_sentiment
from core.utils import extract_keywords

class SocialIntelligenceEngine:

    def __init__(self, posts):
        self.posts = posts
        self.results = []

    def analyze(self):
        analyzed = []

        for post in self.posts:
            sentiment = get_sentiment(post)

            analyzed.append({
                "text": post,
                "sentiment": sentiment["label"],
                "score": sentiment["score"]
            })

        self.results = analyzed
        return analyzed

    def trend_analysis(self):
        keywords = extract_keywords(self.posts)

        top_trends = keywords.most_common(10)

        return [
            {"keyword": k, "count": v}
            for k, v in top_trends
        ]

    def intelligence_summary(self):
        total = len(self.results)

        pos = len([r for r in self.results if r["sentiment"] == "positive"])
        neg = len([r for r in self.results if r["sentiment"] == "negative"])
        neu = total - pos - neg

        return {
            "total_posts": total,
            "positive": pos,
            "negative": neg,
            "neutral": neu,
        }
