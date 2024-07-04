#!/usr/bin/python3
"""
Contains the top_ten function
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the top ten hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    r = requests.get(
        'http://www.reddit.com/r/{}/hot.json'.format(subreddit),
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"},
        params={
            'limit': 10}).json()

    posts = r.get('data', {}).get('children', None)

    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        print(None)
        return

    for post in posts:
        print(post.get('data', {}).get('title', None))
