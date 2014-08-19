#set up the endpoint URLs:
API_URL = "https://api.twitter.com"
REQUEST_TOKEN_URL = API_URL + "/oauth/request_token"
AUTHORIZE_URL = API_URL + "/oauth/authorize?oauth_token={request_token}"
ACCESS_TOKEN_URL = API_URL + "/oauth/access_token"
TIMELINE_URL = API_URL + "/1.1/statuses/home_timeline.json"
#the rest are for the twitter extension
RECENT_RETWEET_URL = API_URL + "/1.1/statuses/retweets/{tweet_id}.json"
GET_TWEET_URL = API_URL + "/1.1/statuses/show/{tweet_id}.json"
RETWEET_URL = API_URL + "/1.1/statuses/retweet/{tweet_id}.json"