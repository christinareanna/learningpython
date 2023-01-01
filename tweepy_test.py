import tweepy
import config 
from twython import Twython, TwythonError

twitter = Twython(config.api_key, config.api_secret, config.bearer_token, config.access_token, config.token_secret)


client = tweepy.Client(bearer_token=config.bearer_token)

query = '#happynewyear2023 -is:retweet lang:en'
tweets = client.search_recent_tweets(query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

for tweet in tweets.data:
    print(tweet.text)
    if len(tweet.context_annotations) > 0:
        print(tweet.context_annotations)
