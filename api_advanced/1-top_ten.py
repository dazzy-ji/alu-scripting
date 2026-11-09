#!/usr/bin/python3
"""
Module to print the titles of the first 10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints titles of the first 10 hot posts."""
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/custom_user)"
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )

        if response.status_code == 200:
            data = response.json().get("data", {})
            children = data.get("children", [])

            if not children:
                print(None)
                return

            for child in children:
                print(child.get("data", {}).get("title"))
        else:
            print(None)
    except Exception:
        print(None)
