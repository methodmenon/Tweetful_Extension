import requests
import json
import sys
import argparse
 
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

def tweet(status):
    "Tweets a message -- Authenticating user's current status"
    auth = authorization.authorize()
    tweet_url = TWEET_URL
    tweet_url = tweet_url.format(status = status)
    return requests.post(tweet_url, auth=auth)




 
def main():
    """ Main function """
    auth = authorization.authorize()
    parser = argparse.ArgumentParser()
    parser.add_argument("tweet_id", type = str, help = "Enter the tweet id for a tweet you are interested in")
    parser.add_argument("-status")
    #prompt the user to enter the tweet_id
    #user_input_tweet_id = raw_input("Please enter the id of the tweet you are interested in: ")
    print("Getting the contents of the tweet")
    response = get_tweet(tweet_id)
    print json.dumps(response.json(), indent=4)
    #Prompt the user if they wish to retweet this tweet or try another tweet id
    print("Please note that you cannot retweet a tweet more than once!")
    user_input_retweet = raw_input("Type Y if you would like to retweet this tweet.\nType anything else if you do not: ")
    if (user_input_retweet == "Y"):
        response = retweet(tweet_id)
        print json.dumps(response.json(), indent=4)
    else:
        print"I see you don't find this interesting!\nYou should find another tweet!"
    if (args.status >= 1):
        response = tweet(status)
        print json.dumps(response.json(), indent=4)
 
if __name__ == "__main__":
    main()