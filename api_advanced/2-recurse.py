#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API and
returns a list containing the titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API to retrieve the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve hot articles from.
        hot_list (list, optional): The list to store the hot article titles. Defaults to None,
                                   which initializes an empty list.
        after (str, optional): The "after" parameter to fetch the next page of hot articles.
                               Defaults to None.

    Returns:
        list or None: A list of hot article titles, or None if the subreddit is invalid or
                      there are no hot articles.
    """
    # Initialize hot_list as an empty list if it is None
    if hot_list is None:
        hot_list = []

    # Construct the URL to the Reddit API endpoint for hot posts of the given
    # subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set up query parameters for pagination
    params = {'after': after} if after else {}

    # Set the User-Agent header to mimic a common web browser to avoid being
    # blocked by the Reddit API
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

    try:
        # Make a GET request to the constructed URL using the requests.get()
        # method
        response = requests.get(
            url,
            params=params,
            headers=headers,
            allow_redirects=False)
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
    except requests.exceptions.RequestException:
        # If the request fails, return None
        return None

    # Parse the JSON response
    data = response.json()
    # Extract the "children" (i.e., the hot posts) from the JSON response
    children = data['data']['children']

    if not children:
        # If the "children" list is empty and hot_list is still empty, return None
        # Otherwise, return the accumulated hot_list
        return None if not hot_list else hot_list

    # Iterate over the hot posts and append the title of each post to hot_list
    for post in children:
        hot_list.append(post['data']['title'])

    # Get the "after" parameter to fetch the next page of hot articles
    after = data['data']['after']

    if after:
        # If there is a next page, call the function recursively
        return recurse(subreddit, hot_list, after)
    else:
        # If there are no more pages, return the accumulated hot_list
        return hot_list
