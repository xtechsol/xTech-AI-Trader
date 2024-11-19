import tweepy
import time
from tweepy import TweepError, RateLimitError

# Authentication setup
def auth():
    consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
    consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
    access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
    access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    try:
        api.verify_credentials()
        print("Authentication OK")
    except Exception as e:
        print(f"Error during authentication: {e}")
        raise e
    
    return api

# Function to handle rate limiting
def handle_rate_limit(api, method, *args, **kwargs):
    try:
        return method(*args, **kwargs)
    except RateLimitError:
        print("Rate limit exceeded. Waiting...")
        time.sleep(15 * 60)  # Wait for 15 minutes
        return handle_rate_limit(api, method, *args, **kwargs)  # Try again

# Function to fetch user timeline
def fetch_user_timeline(api, screen_name, count=200):
    tweets = []
    for page in tweepy.Cursor(api.user_timeline, screen_name=screen_name, count=count, tweet_mode="extended").pages():
        tweets.extend(page)
        if len(tweets) >= 3200:  # Twitter API limit for timeline tweets
            break
    return tweets

# Function to search tweets
def search_tweets(api, query, count=100):
    tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, count=count, tweet_mode="extended").items():
        tweets.append(tweet)
    return tweets

# Function to process tweets
def process_tweet(tweet):
    # Example processing, you can extend this as needed
    print(f"@{tweet.user.screen_name}: {tweet.full_text}")

# Main function to demonstrate usage
def main():
    api = auth()

    # Fetch user timeline
    screen_name = "@elonmusk"  # Example user
    user_timeline = handle_rate_limit(api, fetch_user_timeline, api, screen_name)
    print(f"Fetched {len(user_timeline)} tweets from {screen_name}")
    for tweet in user_timeline[:5]:  # Process first 5 tweets as an example
        process_tweet(tweet)

    # Search for tweets
    search_query = "#Tesla -filter:retweets"  # Example query
    search_results = handle_rate_limit(api, search_tweets, api, search_query)
    print(f"Fetched {len(search_results)} tweets matching '{search_query}'")
    for tweet in search_results[:5]:  # Process first 5 search results as an example
        process_tweet(tweet)

    # Example of handling rate limits in a loop
    try:
        for i in range(10):  # Attempt to fetch 10 pages of tweets
            user_timeline = handle_rate_limit(api, api.user_timeline, id=screen_name, count=200, page=i)
            for tweet in user_timeline:
                process_tweet(tweet)
                if tweet.id == user_timeline[-1].id:  # Check if we've looped back to the first tweet of the page
                    break
            if len(user_timeline) < 200 or tweet.id == user_timeline[-1].id:
                break  # No more pages to fetch
    except TweepError as e:
        print(f"Failed to retrieve tweets: {e}")

if __name__ == "__main__":
    main()
