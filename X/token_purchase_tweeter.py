import tweepy
import os

from setuptools import setup, find_packages

setup(
    name='xTechTrader',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'tweepy']

class TokenPurchaseTweeter:
    def __init__(self):
        # Twitter authentication
        self.auth = tweepy.OAuthHandler(os.environ['TWITTER_CONSUMER_KEY'], os.environ['TWITTER_CONSUMER_SECRET'])
        self.auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
        self.api = tweepy.API(self.auth)

    def tweet_purchase(self, token_address, amount_in_sol, tokens_received, reason):
        """
        Tweet about a token purchase.

        :param token_address: The address of the token purchased
        :param amount_in_sol: The amount of SOL spent
        :param tokens_received: The number of tokens received
        :param reason: The AI's reason for making this purchase
        """
        tweet_message = f"""
🚨 Token Purchase Alert 🚨
- Token Address: {token_address[:6]}...{token_address[-4:]}
- Spent: {amount_in_sol} SOL
- Received: {tokens_received} tokens
Reason for Purchase: {reason}
        """
        
        self.api.update_status(tweet_message)
