#!/usr/bin/python3
"""
This script queries the Reddit API and returns
number of subscribers in given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns number of subscribers in a given subreddit

    Args:
    subreddit (str): Name of subreddit to query

    Returns:
    int: Total number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {"User-Agent": "my_agent/0.0.1"}
    response = requests.get(url, headers=user_agent, allow_redirects=False)
    if response.status_code != 200:
        return 0

    data = response.json().get("data")
    return data.get("subscribers")
