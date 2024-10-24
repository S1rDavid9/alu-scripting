#!/usr/bin/python3
"""1-top_ten.py"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "MyRedditApp/0.1 (by u/yourusername)"}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is not valid (status code != 200)
    if response.status_code != 200:
        print("None")
        return

    # Try to extract data
    try:
        posts = response.json().get("data", {}).get("children", [])
        if not posts:
            print("None")
            return

        # Print titles of the first 10 hot posts
        for post in posts[:10]:  # Ensure we only print 10 items
            print(post.get("data", {}).get("title"))
    except Exception:
        print("None")
