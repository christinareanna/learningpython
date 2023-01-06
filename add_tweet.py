# import tweepy
# import config
# from twython import Twython, TwythonError

# twitter = Twython(config.consumer_key, config.consumer_secret,
#                   config.access_token, config.token_secret)

# client = tweepy.Client(consumer_key=config.consumer_key,
#                        consumer_secret=config.consumer_secret,
#                        access_token=config.access_token,
#                        access_token_secret=config.token_secret)

# Replace the text with whatever you want to Tweet about
# response = client.create_tweet(text='this is a test tweet!!')

# print(response)

import tweepy
import config

consumer_key = config.api_key
consumer_secret_key = config.api_secret
access_token = config.access_token
token_secret = config.token_secret

# client = tweepy.Client(consumer_key=config.client_key,
#                        consumer_secret=config.client_secret,
#                        access_token=config.access_token,
#                        access_token_secret=config.token_secret)

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, token_secret)
api = tweepy.API(auth)

api.update_status("This is a test tweet")
# try:
#     api.verify_credentials()
#     print("Authentication Successful")
# except:
#     print("Authentication Error")

# response = client.create_tweet(text='this is a test tweet')

# print(response)