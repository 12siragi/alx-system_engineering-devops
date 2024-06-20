#!/usr/bin/python3
"""
Prints the titles of the first 10 hot posts listed for a given subreddit
"""

from requests import get

def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    If not a valid subreddit, print None.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'Mozilla/5.0 (compatible; Reddit API query)'}
    params = {'limit': 10}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'

    try:
        response = get(url, headers=user_agent, params=params, allow_redirects=False)
        if response.status_code != 200:
            print("None")
            return

        results = response.json()
        posts = results.get('data', {}).get('children', [])

        if not posts:
            print("None")
            return

        for post in posts:
            print(post.get('data', {}).get('title', "None"))

    except Exception:
        print("None")
