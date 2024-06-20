#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of total subscribers for a given
subreddit.
"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of total subscribers for a
    given subreddit.
    
    Args:
    - subreddit (str): The name of the subreddit (without the '/r/' prefix).
    
    Returns:
    - int: Number of subscribers if successful, or 0 if subreddit is invalid or API request fails.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Python/1.0 (Holberton School 0x16 task 0)'}
    
    try:
        response = requests.get(url, headers=headers)
        
        # Handle specific HTTP errors
        if response.status_code == 403:
            print("Access to subreddit information is forbidden (403 Error)")
            return 0
        
        response.raise_for_status()  # Raise an exception for other bad responses (4xx or 5xx)
        
        data = response.json()
        subscriber_count = data['data']['subscribers']
        return subscriber_count
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return 0
    
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return 0
    
    except KeyError:
        print("KeyError: 'subscribers' not found in response data.")
        return 0
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0

# Example usage if run directly
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        print(f"Number of subscribers in r/{subreddit_name}: {number_of_subscribers(subreddit_name)}")
