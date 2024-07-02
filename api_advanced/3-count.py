#!/usr/bin/python3

import requests


def count_words(subreddit, word_list):
    """
    Recursively queries the Reddit API to count the occurrences of the given keywords in the hot articles of a
    subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count.

    Returns:
        None
    """
    def _count_words(after=None):
        """
        Helper function to recursively fetch and count the keywords.
        """
        # Construct the API URL
        url = f'https://api.reddit.com/r/{subreddit}/hot.json'
        if after:
            url += f'?after={after}'

        header = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
        }

        try:
            response = requests.get(url, headers=header)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            # Handle invalid subreddit
            if response.status_code == 404:
                return
            else:
                raise e

        # Extract the article titles from the response
        data = response.json()['data']
        titles = [item['data']['title'].lower() for item in data['children']]

        # Count the keywords
        word_counts = {}
        for word in word_list:
            count = sum(title.count(word.lower()) for title in titles)
            if count > 0:
                word_counts[word.lower()] = count

        # Print the results in the required format
        for word, count in sorted(word_counts.items(), key=lambda x: (-x[1], x[0])):
            print(f"{word} : {count}")

        # Recursive call if there are more pages
        if data['after']:
            _count_words(data['after'])
