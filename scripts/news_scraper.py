import tweepy
import requests
import os
from textblob import TextBlob
from dotenv import load_dotenv

load_dotenv()
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

print(f"NewsAPI Key: {NEWS_API_KEY}")
print(f"Twitter Bearer Token: {TWITTER_BEARER_TOKEN}")

# Tweepy client for Twitter API
client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

def fetch_news():
    url = f"https://newsapi.org/v2/everything?q=bitcoin&language=en&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get("articles", [])
        headlines = [article["title"] for article in articles[:5]]
        return headlines
    return []

def fetch_tweets():
    query = "Bitcoin OR BTC -is:retweet lang:en"
    tweets = client.search_recent_tweets(query=query, max_results=5, tweet_fields=["text"])
    return [tweet.text for tweet in tweets.data] if tweets.data else []

def analyze_sentiment(texts):
    sentiment_score = sum(TextBlob(text).sentiment.polarity for text in texts) / len(texts) if texts else 0
    return "positive" if sentiment_score > 0 else "negative" if sentiment_score < 0 else "neutral"

if __name__ == "__main__":
    news = fetch_news()
    tweets = fetch_tweets()
    sentiment = analyze_sentiment(news + tweets)
    print(f"News Sentiment: {sentiment}")
