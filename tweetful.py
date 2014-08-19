import requests
import json
import sys
 
import authorization
from urls import *


def get_tweet(tweet_id):
    "returns a single tweet, specified by the id parameter"
    auth = authorization.authorize()
    get_tweet_url = GET_TWEET_URL
    get_tweet_url = get_tweet_url.format(tweet_id = tweet_id)
    return requests.get(get_tweet_url, auth=auth)

def retweet(tweet_id):
    "retweets a tweet"
    auth = authorization.authorize()
    retweet_url = RETWEET_URL
    retweet_url = retweet_url.format(tweet_id = tweet_id)
    return requests.get(retweet_url, auth=auth)



 
def main():
    """ Main function """
    #tweet id for the moment: 500081119417470976
    auth = authorization.authorize()
    response = get_tweet(sys.argv[1])
    print json.dumps(response.json(), indent=4)
 
if __name__ == "__main__":
    main()