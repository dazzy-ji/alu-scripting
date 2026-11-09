#!/usr/bin/python3
"""
Recursive module to query Reddit API and return titles of all hot articles.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively fetches titles of all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting:api_advanced:v1.0 (by /u/dazzy)"}
    params = {"after": after} if after else {}

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code != 200:
        return None

    data = response.json().get("data", {})
    children = data.get("children", [])
    after = data.get("after")

    for child in children:
        hot_list.append(child.get("data", {}).get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
