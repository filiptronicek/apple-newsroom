from twython import Twython
from os import environ as env



def tweet(tweetText:str):
    if env.get('CONSUMER_KEY') is None:
        from creds import API_key, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
    else:
        CONSUMER_KEY = env.get('CONSUMER_KEY')
        CONSUMER_SECRET = env.get('CONSUMER_SECRET')
        ACCESS_KEY = env.get('ACCESS_KEY')
        ACCESS_SECRET = env.get('ACCESS_SECRET')

    twitter_api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)
    twitter_api.update_status(status=tweetText)