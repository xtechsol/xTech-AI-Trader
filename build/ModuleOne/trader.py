from data_collector import DataCollector
from ai_model import AIModel
from solana.rpc.api import Client
from solana.publickey import PublicKey
import os
import time

class CryptoTrader:
    def __init__(self, config):
        self.config = config
        self.collector = DataCollector(config)
        self.ai = AIModel(self.collector)
        self.solana_client = Client("https://api.mainnet-beta.solana.com")
        self.wallet = PublicKey(os.getenv('SOLANA_WALLET'))

    def fetch_and_learn(self):
        market_data, sentiment = self.collector.collect_data()
        X_train, X_test, y_train, y_test = self.ai.prepare_data(market_data, sentiment)
        self.ai.train_model(X_train, X_test, y_train, y_test)

    def execute_trade(self, action, amount):
        if action == "buy":
            # Placeholder for buy transaction via Solana
            print(f"Executing buy order for {amount} SOL")
            # Here you'd actually send a transaction to buy SOL or a token
            return True
        elif action == "sell":
            # Placeholder for sell transaction via Solana
            print(f"Executing sell order for {amount} SOL")
            # Here you'd actually send a transaction to sell SOL or a token
            return True
        return False

    def tweet_action(self, action, amount):
        import tweepy
        auth = tweepy.OAuthHandler(self.config['twitter']['consumer_key'], self.config['twitter']['consumer_secret'])
        auth.set_access_token(self.config['twitter']['access_token'], self.config['twitter']['access_token_secret'])
        api = tweepy.API(auth)
        message = f"AI has decided to {action} {amount} SOL due to market conditions."
        api.update_status(message)

    def run(self):
        while True:
            self.fetch_and_learn()
            market_data, sentiment = self.collector.collect_data()
            latest_features = self.ai.scaler.transform(market_data[['Price']].diff().fillna(0).values[-1].reshape(1, -1))
            sentiment_feature = np.array([sentiment])
            combined_features = np.hstack((latest_features, sentiment_feature))
            action = self.ai.predict(combined_features)
            
            if action == "buy":
                amount = 1  # Example amount in SOL
                if self.execute_trade(action, amount):
                    self.tweet_action(action, amount)
            elif action == "sell":
                amount = 1  # Example amount in SOL
                if self.execute_trade(action, amount):
                    self.tweet_action(action, amount)
            
            time.sleep(60 * 60)  # Wait for an hour

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
    trader = CryptoTrader(load_config())
    trader.run()
