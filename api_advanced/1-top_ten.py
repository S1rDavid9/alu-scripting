#!/usr/bin/python3
"""1-top_ten.py"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyRedditApp/0.1 (by u/yourusername)"}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check for a valid response
    if response.status_code != 200:
        print(None)
        return

    # Try to extract the data from the response
    try:
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print(None)
            return

        # Print the titles of the first 10 hot posts
        for post in posts:
            print(post.get("data", {}).get("title"))
    except (KeyError, ValueError):
        print(None)
