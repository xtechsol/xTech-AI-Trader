from solana.rpc.api import Client
import pandas as pd
import tweepy
import os
from datetime import datetime, timedelta

class DataCollector:
    def __init__(self, config):
        self.config = config
        self.twitter_api = self.initialize_twitter_api()
        self.solana_client = Client("https://api.mainnet-beta.solana.com")
        self.market_data = None
        self.tweets = []
        self.solana_account = os.getenv('SOLANA_ACCOUNT')

    def initialize_twitter_api(self):
        auth = tweepy.OAuthHandler(self.config['twitter']['consumer_key'], self.config['twitter']['consumer_secret'])
        auth.set_access_token(self.config['twitter']['access_token'], self.config['twitter']['access_token_secret'])
        return tweepy.API(auth)

    def get_solana_prices(self, since_days=7):
        end_time = int(datetime.now().timestamp())
        start_time = int((datetime.now() - timedelta(days=since_days)).timestamp())
        response = self.solana_client.get_signatures_for_address(
            self.solana_account, 
            limit=1000,  # Adjust limit according to your needs
            before=None,
            until=end_time,
            commitment="confirmed"
        )
        prices = []
        times = []
        for signature in response['result']:
            tx = self.solana_client.get_transaction(signature['signature'], encoding="jsonParsed")
            for instruction in tx['result']['transaction']['message']['instructions']:
                if 'parsed' in instruction and instruction['parsed']['type'] == 'transfer':
                    parsed = instruction['parsed']
                    if parsed['info']['destination'] == self.solana_account:
                        # Here you would extract the price information, which is a placeholder in this example
                        prices.append(1)  # Placeholder for price, you'd need to fetch real-time/token price data
                        times.append(datetime.fromtimestamp(int(signature['blockTime'])))
        self.market_data = pd.DataFrame({'Price': prices, 'Time': times})

    def get_tweets(self, query, count=100):
        for tweet in tweepy.Cursor(self.twitter_api.search_tweets, q=query, lang="en").items(count):
            self.tweets.append(tweet.text)

    def analyze_sentiment(self):
        from textblob import TextBlob
        sentiment_scores = [TextBlob(tweet).sentiment.polarity for tweet in self.tweets]
        average_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0.0
        return average_sentiment

    def collect_data(self, query='Solana OR $SOL -filter:retweets', since_days=7):
        self.get_solana_prices(since_days)
        self.get_tweets(query)
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
    market_data, sentiment = collector.collect_data()
    print("Market Data:", market_data)
    print("Sentiment:", sentiment)
