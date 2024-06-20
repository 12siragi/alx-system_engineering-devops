#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; Reddit API query by /u/yourusername)'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
