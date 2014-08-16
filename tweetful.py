import requests
import json
import sys
 
import authorization
from urls import *

def get_retweets(tweet_id):
    auth = authorization.authorize()
    """retrieve up to the last 100 retweets of a particular tweet specified by the id parameter"""
    retweet_url = RETWEET_URL
    retweet_url = retweet_url.format(tweet_id = tweet_id)
    return requests.get(retweet_url, auth=auth)
 
def main():
    """ Main function """
    #retweet id for the moment: 500081119417470976
    auth = authorization.authorize()
    response = get_retweets(sys.argv[1])
    #response = requests.get(TIMELINE_URL, auth=auth)
    print json.dumps(response.json(), indent=4)
 
if __name__ == "__main__":
    main()