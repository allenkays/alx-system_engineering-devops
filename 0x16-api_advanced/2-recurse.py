#!/usr/bin/python3
"""
Function to query the Reddit API and return a list
of titles of all hot articles for a given subreddit
recursively
"""

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Returns a list of hot articles recursively

    Args:
    subreddit (str): Name of subreddit to query

    Returns:
    list (list): list of titles per page
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "my_user_agent/0.0"}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json().get("data")
    after = data.get("after")
    count += data.get("dist")
    titles = response.json().get("data").get("children")
    for c in titles:
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
