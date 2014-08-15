import requests
import json
 
import authorization
from urls import *
 
def main():
    """ Main function """
    auth = authorization.authorize()
 
    response = requests.get(TIMELINE_URL, auth=auth)
    print json.dumps(response.json(), indent=4)
 
if __name__ == "__main__":
    main()