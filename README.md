# 🧠 Social Intelligence Engine - A Streamlit version

A lightweight AI-powered system that simulates social media intelligence by analyzing trends, sentiment, and topic momentum from social posts.

## 🚀 Features
- Social post ingestion (mock + optional Reddit API)
- Sentiment analysis using VADER
- Trend detection based on keyword frequency
- Intelligence scoring engine
- Interactive dashboard (Streamlit)

## 🧱 Tech Stack
- Python
- Streamlit
- VADER Sentiment
- Pandas / NumPy

## Architecture

                ┌──────────────────┐
                │ React Dashboard  │
                └────────┬─────────┘
                         │
                  FastAPI Gateway
                         │
 ┌──────────────┬────────┼────────┬──────────────┐
 │              │        │        │              │
 ▼              ▼        ▼        ▼              ▼

Data       AI Engine   Trend   Reporting   Notification
Collector             Engine     Engine       Engine

 │
 ▼

PostgreSQL
 │
 ▼
Redis Cache
 │
 ▼
Vector Database

---
## 📦 Installation

```bash
pip install -r requirements.txt
