#!/usr/bin/python3
"""
Contains the recurse function
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list of all hot post titles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): The list to store the hot post titles. Defaults to an empty list.
        after (str, optional): The "after" parameter to fetch the next page of hot posts. Defaults to None.

    Returns:
        list: A list of hot post titles, or None if the subreddit is invalid or there are no hot posts.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    r = requests.get(
        'http://www.reddit.com/r/{}/hot.json'.format(subreddit),
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"},
        allow_redirects=False,
        params={
            'after': after}).json()

    after = r.get('data', {}).get('after', None)
    posts = r.get('data', {}).get('children', None)

    if posts is None or (len(posts) > 0 and posts[0].get('kind') != 't3'):
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        for post in posts:
            hot_list.append(post.get('data', {}).get('title', None))

    if after is None:
        if len(hot_list) == 0:
            return None
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)
