#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    This function makes an HTTP GET request to the Reddit API to fetch information
    about the given subreddit. The number of subscribers is returned if the subreddit
    exists. If the subreddit is invalid, it will return 0. It ensures not to follow
    redirects, as invalid subreddits might redirect to search results.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers of the subreddit. Returns 0 if the subreddit
             does not exist or if the request fails.

    Usage example:
        >>> number_of_subscribers("python")
        3456789

        >>> number_of_subscribers("invalid_subreddit")
        0
    """
    
    # The Reddit API endpoint for getting subreddit details
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set custom headers including a User-Agent to comply with Reddit API requirements
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MyBot/1.0; +http://mybot.com/bot.html)"
    }
    
    try:

        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request is successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and extract subscriber count
            data = response.json()  # Parse the response JSON
            return data['data']['subscribers']  # Return the number of subscribers
        else:
            # Return 0 if the subreddit is invalid or the request fails
            return 0
    except Exception as e:
        # Handle exceptions such as connection errors or request issues
        return 0
