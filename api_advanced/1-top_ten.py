#!/usr/bin/python3
"""Print the titles of the first 10Hot Posts"""

import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Queries the Reddit API recursively, parses the title of all hot articles,
    and prints a sorted count of given keywords (case-insensitive).

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): List of keywords to count occurrences of.
        word_count (dict): Dictionary to store the count of keywords.
        after (str): The 'after' key for pagination (defaults to None).
    """
    # Base URL for querying the Reddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyRedditApp/0.1 (by u/yourusername)"}
    params = {"limit": 100, "after": after}

    # Make the request to Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if subreddit is valid
    if response.status_code != 200:
        return None  # Explicitly return None if the subreddit is invalid

    # Extract JSON data from the response
    data = response.json().get("data", {})
    children = data.get("children", [])
    after = data.get("after", None)  # Pagination token

    # Normalize word_list to lower case
    word_list = [word.lower() for word in word_list]

    # Loop through each post
    for post in children:
        title = post.get("data", {}).get("title", "").lower()  # Get the title and normalize it

        # Split the title into words and count occurrences of keywords in word_list
        for word in title.split():
            # Strip non-alphanumeric characters from each word
            word = word.strip('.,!?_-')
            if word in word_list:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    # If there's more data (pagination), recursively call the function
    if after is not None:
        return count_words(subreddit, word_list, word_count, after)

    # Once all pages are processed, sort and print the results
    if word_count:
        sorted_counts = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
        for word, count in sorted_counts:
            print(f"{word}: {count}")
    else:
        print("OK")  # For both valid and empty subreddits, we output "OK"

