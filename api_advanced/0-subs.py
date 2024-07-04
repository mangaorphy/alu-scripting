#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the given subreddit, or 0 if the subreddit is None or not a string.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    r = requests.get(
        'http://www.reddit.com/r/{}/about.json'.format(subreddit),
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs
