import requests
import json
import sys
 
import authorization
from urls import *

def get_retweets(tweet_id):
    auth = authorization.authorize()
    """retrieve up to the last 100 retweets of a particular tweet specified by the id parameter"""
    recent_retweet_url = RECENT_RETWEET_URL
    recent_retweet_url = recent_retweet_url.format(tweet_id = tweet_id)
    return requests.get(recent_retweet_url, auth=auth)

#def retweet(tweet_id):

 
def main():
    """ Main function """
    #retweet id for the moment: 500081119417470976
    auth = authorization.authorize()
    response = get_retweets(sys.argv[1])
    #response = requests.get(TIMELINE_URL, auth=auth)
    print json.dumps(response.json(), indent=4)
 
if __name__ == "__main__":
    main()