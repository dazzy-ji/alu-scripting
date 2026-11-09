#!/usr/bin/python3
"""
Module to print the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Queries Reddit API and prints the titles of the first 10 hot posts."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "linux:alu-scripting:v1.0.0 (by /u/dazzy-ji)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print(None)
            return

        data = response.json().get("data", {})
        posts = data.get("children", [])
        
        if not posts:
            print(None)
            return

        for post in posts:
            title = post.get("data", {}).get("title")
            if title:
                print(title)
    except Exception:
        print(None)
