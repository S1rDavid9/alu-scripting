#!/usr/bin/python3
"""
A module that prints the titles of the first 10 hot posts from a given subreddit.

This module contains a single function, `top_ten(subreddit)`, that fetches the
titles of the first 10 hot posts from the Reddit API for a specified subreddit.

Requirements:
- requests module (install with `pip install requests` if not already installed)

Usage:
- Call `top_ten(subreddit)`, where `subreddit` is the name of the subreddit 
  to query. If the subreddit is valid, it will print the titles of the first 10 
  hot posts; otherwise, it will print `None`.
"""

import requests

def top_ten(subreddit):
    """
    Fetch and print the titles of the first 10 hot posts from a given subreddit.
    
    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    None: The function prints the titles directly or prints `None` if the subreddit is invalid.

    The function sends a GET request to the Reddit API with a custom User-Agent
    header. If successful, it prints the titles of the first 10 hot posts. If the 
    request fails (e.g., if the subreddit does not exist), it prints `None`.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response status is OK
    if response.status_code == 200:
        json_data = response.json()
        posts = json_data.get('data', {}).get('children', [])
        
        # Check if posts are available and print each title
        if posts:
            for post in posts:
                print(post.get('data', {}).get('title'))
        else:
            print(None)
    else:
        # If subreddit doesn't exist or there was an error, print None
        print(None)
