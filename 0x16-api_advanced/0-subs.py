#!/usr/bin/python3
"""
This module queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    This function queries the Reddit API and returns the number of subscribers
    """

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    req = requests.get(url, headers=headers, allow_redirects=False)
    if req.status_code != 200:
        return 0
    return req.json().get("data").get("subscribers")
