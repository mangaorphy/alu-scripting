#!/usr/bin/python3

import requests


def number_of_subscribers(subreddit):
    # Set the custom User-Agent
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

    # Construct the URL for the subreddit API
    url = f"https://api.reddit.com/r/{subreddit}/about"

    # Send a GET request to the API with the custom User-Agent
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON and extract the number of subscribers
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    elif response.status_code == 404:
        # Return 0 for invalid subreddits (status code 404)
        print(f"The subreddit '{subreddit}' does not exist.")
        return 0
    else:
        # Return 0 for other error responses
        return 0
