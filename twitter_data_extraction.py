import os
import tweepy
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_SECRET_API_KEY = os.getenv("TWITTER_SECRET_API_KEY")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")


client = tweepy.Client(TWITTER_BEARER_TOKEN)
# Replace with your own search query
query = 'from:suhemparack -is:retweet'

tweets = client.search_all_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)



# auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_SECRET_API_KEY)
# auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

# api = tweepy.API(auth)

# tweets = api.user_timeline(screen_time = '@elonmusk',
#                            count = 10,
#                            include_rts = False,
#                            tweet_mode = 'extended')
# print(tweets)