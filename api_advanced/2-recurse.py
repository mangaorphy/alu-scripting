#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API to retrieve the titles of hot articles
    for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list, optional): A list to store the hot article titles.
            If not provided, an empty list will be created.
        after (str, optional): A pagination token to fetch the next page of results.

    Returns:
        list or None: A list of hot article titles, or None if the subreddit is invalid.
    """
    global response
    if hot_list is None:
        hot_list = []

    # Construct the API URL
    url = f'https://api.reddit.com/r/{subreddit}/hot.json'
    if after:
        url += f'?after={after}'

    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    # Make the API request
    try:
        response = requests.get(url, headers=header)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # Handle invalid subreddit
        if response.status_code == 404:
            return None
        else:
            raise e

    # Extract the article titles from the response
    data = response.json()['data']
    hot_list.extend([item['data']['title'] for item in data['children']])

    # Check if there are more pages of results
    if data['after']:
        return recurse(subreddit, hot_list, data['after'])
    else:
        return hot_list
