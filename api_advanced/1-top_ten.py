#!/usr/bin/python3
"""
Module to print the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Queries Reddit API and prints the titles of the first 10 hot posts."""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api_advanced:v1.0 (by /u/dazzy)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get("data", {})
        posts = data.get("children", [])
        for post in posts:
            print(post.get("data", {}).get("title"))
    else:
        print(None)
