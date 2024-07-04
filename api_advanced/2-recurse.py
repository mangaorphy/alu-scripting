import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API to retrieve the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve hot articles from.
        hot_list (list, optional): The list to store the hot article titles. Defaults to an empty list.
        after (str, optional): The "after" parameter to fetch the next page of hot articles. Defaults to None.

    Returns:
        list or None: A list of hot article titles, or None if the subreddit is invalid or there are no hot articles.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after} if after else {}
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, params=params, headers=headers, allow_redirects=False)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        return None

    data = response.json()
    children = data['data']['children']

    if not children:
        return None if not hot_list else hot_list

    for post in children:
        hot_list.append(post['data']['title'])

    after = data['data']['after']
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
