#!/usr/bin/python3
"""
    This module queries the Reddit API and
    prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    This function queries the Reddit API and
    prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        None if subreddit is not found.
    else:
        The titles of the first 10 hot posts listed for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = {"User-Agent": "Mozilla/5.0"}
    req = requests.get(url, headers=headers, allow_redirects=False)

    if req.status_code != 200:
        print(None)
        return 0

    hot_post = req.json().get("data").get("children")
    for topTen in hot_post:
        print(topTen.get("data").get("title"))
