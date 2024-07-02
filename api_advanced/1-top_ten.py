#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """
    Retrieve and print the titles of the top 10 posts in a given subreddit.

    Parameters:
        subreddit (str): The name of the subreddit.

    Returns:
        None

    """
    # Set the custom User-Agent
    header = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"}

    # Construct the URL for the subreddit API
    url = f"https://api.reddit.com/r/{subreddit}/hot"
    # Send a GET request to the API with the custom User-Agent
    response = requests.get(url, headers=header, allow_redirects=False)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON and extract the titles of the first 10 posts
        data = response.json()
        posts = data["data"]["children"]

        # Print the titles of the first 10 posts
        for i in range(10):
            if i < len(posts):
                post_title = posts[i]["data"]["title"]
                print(f"{post_title}")
            else:
                break
    else:
        # Print None for invalid subreddits or error responses
        print(None)
