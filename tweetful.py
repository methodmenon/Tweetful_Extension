import requests
import json
import sys
import argparse
 
import authorization
from urls import *


def get_tweet(tweet_id, auth):
    "returns a single tweet, specified by the id parameter"
    #auth = authorization.authorize()
    get_tweet_url = GET_TWEET_URL
    get_tweet_url = get_tweet_url.format(tweet_id = tweet_id)
    return requests.get(get_tweet_url, auth=auth)

def retweet(tweet_id, auth):
    "retweets a tweet"
    #auth = authorization.authorize()
    retweet_url = RETWEET_URL
    retweet_url = retweet_url.format(tweet_id = tweet_id)
    return requests.post(retweet_url, auth=auth)

def tweet(message, auth):
    "Tweets a message"
    tweet_url = TWEET_URL
    #required parameter for POST data form is the status
    data = {'status': message}
    return requests.post(tweet_url, data=data, auth=auth)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tweet_id", help = "Enter the tweet id for a tweet you are interested in", action = "store_true")
    parser.add_argument("--tweet", help = "Update your twitte status", action = "store_true")
    args = parser.parse_args()
    
    if (args.tweet_id):
        auth = authorization.authorize()
        #prompt the user to enter the tweet_id
        tweet_id = raw_input("Please enter the id of the tweet you are interested in: ")
        print("Getting the contents of the tweet")
        response = get_tweet(tweet_id, auth)
        print json.dumps(response.json(), indent=4)
        #Prompt the user if they wish to retweet this tweet or try another tweet id
        print("Please note that you cannot retweet a tweet more than once!")
        user_input_retweet = raw_input("Type Y if you would like to retweet this tweet.\nType anything else if you do not: ")
        if (user_input_retweet == "Y"):
            response = retweet(tweet_id, auth)
            print json.dumps(response.json(), indent=4)
        else:
            print"I see you don't find this interesting!\nYou should find another tweet!"

    if (args.tweet):
        auth = authorization.authorize()
        user_input = raw_input("Please type your status: ")
        #leave blank if you don't want to tweet anything
        if (user_input == ""):
            print "I guess you have nothing to tweet"
        else:
            response = tweet(user_input, auth)
            print json.dumps(response.json(), indent=4)

if __name__ == "__main__":
    main()
