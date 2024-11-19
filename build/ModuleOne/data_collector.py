import yfinance as yf
import pandas as pd
import tweepy
import os
from datetime import datetime, timedelta

class DataCollector:
    def __init__(self, config):
        self.config = config
        self.twitter_api = self.initialize_twitter_api()
        self.market_data = None
        self.tweets = []

    def initialize_twitter_api(self):
        auth = tweepy.OAuthHandler(self.config['twitter']['consumer_key'], self.config['twitter']['consumer_secret'])
        auth.set_access_token(self.config['twitter']['access_token'], self.config['twitter']['access_token_secret'])
        return tweepy.API(auth)

    def get_market_data(self, symbol, start_date, end_date):
        ticker = yf.Ticker(symbol)
        data = ticker.history(start=start_date, end=end_date)
        data['Date'] = data.index.date
        self.market_data = data

    def get_tweets(self, query, count=100):
        for tweet in tweepy.Cursor(self.twitter_api.search_tweets, q=query, lang="en").items(count):
            self.tweets.append(tweet.text)

    def analyze_sentiment(self):
        # Placeholder for sentiment analysis
        from textblob import TextBlob
        sentiment_scores = [TextBlob(tweet).sentiment.polarity for tweet in self.tweets]
        if sentiment_scores:
            average_sentiment = sum(sentiment_scores) / len(sentiment_scores)
        else:
            average_sentiment = 0.0
        return average_sentiment

    def collect_data(self, symbols, since_days=7):
        end_date = datetime.now()
        start_date = end_date - timedelta(days=since_days)
        for symbol in symbols:
            self.get_market_data(symbol, start_date, end_date)
            self.get_tweets(f'${symbol}')
        sentiment = self.analyze_sentiment()
        return self.market_data, sentiment

def load_config():
    return {
        'twitter': {
            'consumer_key': os.getenv('TWITTER_CONSUMER_KEY'),
            'consumer_secret': os.getenv('TWITTER_CONSUMER_SECRET'),
            'access_token': os.getenv('TWITTER_ACCESS_TOKEN'),
            'access_token_secret': os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
        }
    }

if __name__ == "__main__":
    collector = DataCollector(load_config())
    symbols = ['BTC-USD', 'ETH-USD']  # Example symbols
    market_data, sentiment = collector.collect_data(symbols)
    print("Market Data:", market_data)
    print("Sentiment:", sentiment)
