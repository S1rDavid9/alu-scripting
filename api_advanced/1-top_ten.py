#!/usr/bin/python3
"""1-top_ten.py"""

import requests

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for a given subreddit. If the subreddit is invalid or doesn't exist,
    it prints 'None'.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None

    Example usage:
        >>> top_ten("python")
        Post 1 title
        Post 2 title
        ...
    """
    
    # API endpoint to fetch hot posts for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Set custom headers to avoid Too Many Requests error and comply with Reddit API's rules
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MyBot/1.0; +http://mybot.com/bot.html)"
    }
    
    try:
        # Send a GET request to Reddit API (no redirects for invalid subreddits)
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request is successful (status code 200)
        if response.status_code == 200:
            # Parse JSON data
            data = response.json()
            # Extract the list of posts from the response
            posts = data.get('data', {}).get('children', [])
            
            # If there are posts, print the titles of the first 10
            for post in posts:
                print(post['data']['title'])
        else:
            # If subreddit is invalid or request fails, print None
            print("None")
    
    except Exception as e:
        # Handle potential exceptions like connection issues
        print("None")
