#!/usr/bin/python3
"""
This script prints the first 10 titles of hot posts
listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Prints titles of top ten hot posts

    Args:
    subreddit (str): name of subreddit to query

    Returns:
    Titles (str): First 10 titles
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "my_agent/0.0.1"}
    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code != 200:
        print(None)
        return
    data = resp.json().get("data")
    [print(x.get("data").get("title")) for x in data.get("children")]
