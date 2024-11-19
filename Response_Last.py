import random
from datetime import datetime
import re

class TweetGenerator:
    # ... (previous code remains the same)

    def generate_wallet_activity_response(self, address, activity_type, amount, token_symbol):
        activity_phrases = {
            'received': [
                f"Deposited {amount} $({token_symbol}) into wallet {address[:6]}...{address[-4:]}. #CryptoReceived #PortfolioUpdate",
                f"Received {amount} $({token_symbol}) - wallet {address[:6]}...{address[-4:]}. #CryptoMovement #IncomingFunds"
            ],
            'sent': [
                f"Sent {amount} $({token_symbol}) from wallet {address[:6]}...{address[-4:]}. #CryptoSent #TransactionUpdate",
                f"Transferred {amount} $({token_symbol}) - wallet {address[:6]}...{address[-4:]}. #CryptoFlow #OutgoingFunds"
            ],
            'swapped': [
                f"Swapped {amount} $({token_symbol}) in wallet {address[:6]}...{address[-4:]}. #CryptoSwap #DExActivity",
                f"Exchanged {amount} $({token_symbol}) - wallet {address[:6]}...{address[-4:]}. #TokenExchange #TradeAlert"
            ]
        }

        if activity_type not in activity_phrases:
            return None

        phrase = random.choice(activity_phrases[activity_type])
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        timestamp = f"\nActivity recorded at {now}"
        
        tweet = f"{phrase}{timestamp}"
        return self.shorten_tweet(tweet)

def generate_buy_tweet(self, token, sol_amount, contract_address):
        return self.generate_tweet('buy', token, sol_amount, None, None, contract_address)

    def generate_sell_tweet(self, token, sol_amount, wallet_balance):
        return self.generate_tweet('sell', token, sol_amount, wallet_balance, None, None)

    def generate_create_tweet(self, token, contract_address):
        return self.generate_tweet('create', token, None, None, None, contract_address)

    def generate_tweet(self, action, token, sol_amount=None, wallet_balance=None, sentiment=None, contract_address=None):
        if action == 'buy':
            phrase = random.choice(self.buy_phrases).format(token, sol_amount)
        elif action == 'sell':
            phrase = random.choice(self.sell_phrases).format(token, sol_amount)
        elif action == 'create':
            phrase = random.choice(self.create_phrases).format(token)
        else:
            return None

        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        timestamp = f"\nTraded at {now}"
        
        if action in ['buy', 'create']:
            tweet = f"{phrase}\n> contract address: {contract_address}"
        elif action == 'sell':
            tweet = f"{phrase}\n> wallet balance: {wallet_balance} SOL"

        tweet += self.add_hashtags()
        if action != 'create':
            tweet += self.add_emoji(action)
            if sentiment:
                sentiment_comment = random.choice(self.sentiment_phrases).format(token, sentiment)
                tweet += f"\n{sentiment_comment}"

        tweet += timestamp

        return self.shorten_tweet(tweet)

    def add_hashtags(self):
        return " " + " ".join(random.sample(self.hashtags, random.randint(2, 5)))

    def add_emoji(self, action):
        emojis = self.emojis.get(action, [])
        return " " + " ".join(random.sample(emojis, random.randint(1, 3)))

    def shorten_tweet(self, tweet):
        max_length = 280
        if len(tweet) <= max_length:
            return tweet
        else:
            lines = tweet.split('\n')
            while len('\n'.join(lines)) > max_length and len(lines) > 1:
                lines.pop()
            return '\n'.join(lines) + "..." if len(tweet) > max_length else tweet

    def customize_tweet(self, tweet, style=None):
        # This method can be extended to modify the tweet's tone or style
        pass
