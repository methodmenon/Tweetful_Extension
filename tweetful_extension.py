import requests
import json

import authorization
from urls import *

def get_retweets():
	auth = authorization.authorize()
	"""retrieve up to the last 100 tweets the from the user"""
	return requests.get(RETWEET_URL, auth=auth)

def main():
    """ Main function """
    auth = authorization.authorize()
    response= get_retweets()
    print json.dumps(response.json(), indent=4)
 
if __name__ == "__main__":
    main()