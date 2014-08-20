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
    return requests.post(retweet_url, auth=auth)



 
def main():
    """ Main function """
    auth = authorization.authorize()
    #prompt the user to enter the tweet_id
    user_input_tweet_id = raw_input("Please enter the id of the tweet you are interested in: ")
    print("Getting the contents of the tweet")
    response = get_tweet(user_input_tweet_id)
    print json.dumps(response.json(), indent=4)
    #Prompt the user if they wish to retweet this tweet or try another tweet id
    print("Please note that you cannot retweet a tweet more than once!")
    user_input_retweet = raw_input("Type Y if you would like to retweet this tweet.\nType anything else if you do not: ")
    if (user_input_retweet == "Y"):
        response = retweet(user_input_tweet_id)
        print json.dumps(response.json(), indent=4)
    else:
        print"I see you don't find this interesting!\nYou should find another tweet!"
 
if __name__ == "__main__":
    main()