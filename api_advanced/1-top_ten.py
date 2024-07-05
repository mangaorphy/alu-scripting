#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and
returns the top 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve the hot posts from.

    Returns:
        None
    """
    # Construct the URL to the Reddit API endpoint for the hot posts of the given subreddit,
    # with the "limit" parameter set to 10 to fetch the first 10 hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set the User-Agent header to mimic a common web browser,
    # to avoid being blocked by the Reddit API
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    try:
        # Make a GET request to the constructed URL using the requests.get() method,
        # and retrieve the JSON response. Set the "allow_redirects" parameter
        # too False to avoid following redirects.
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
    except requests.exceptions.RequestException:
        # If the request fails, print "None" and return
        print(None)
        return

    # Extract the "children" (i.e., the hot posts) from the JSON response
    data = response.json()
    children = data['data']['children']

    if not children:
        # If the "children" list is empty (i.e., there are no hot posts for the given subreddit),
        # print "None" and return
        print(None)
        return

    # Iterate over the hot posts and print the title of each post,
    # but only if the length of the "children" list is 10 or less
    for post in children[:10]:
        print(post['data']['title'])
