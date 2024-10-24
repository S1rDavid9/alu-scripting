#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Define the Reddit API URL for the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Define custom headers with a User-Agent to avoid "Too Many Requests" errors
    headers = {"User-Agent": "Mozilla/5.0"}
    
    try:
        # Make a GET request to the API without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response and return the number of subscribers
            data = response.json()
            return data['data']['subscribers']
        else:
            # If the status code is not 200 (e.g., subreddit not found), return 0
            return 0
    except requests.RequestException:
        # If there is a network or request error, return 0
        return 0

# Example usage:
subreddit_name = "python"  # Replace with the subreddit name
print(number_of_subscribers(subreddit_name))
