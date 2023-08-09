#!/usr/bin/python3
"""
recursive function that queries the Reddit API and
returns a list containing the titles of all hot articles
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recurively queries the Reddit API
    and get all the list of hot titles

    Args:
        subreddit (str): The subreddit to query
        hot_list (list): The list of hot titles

    Returns:
        None if subreddit is not found.
    else:
        The titles of ALL hot posts listed for a given subreddit.
    """

    url = "https://www.reddit.com/r/{}/hot.json?".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    query_string = {"after": after}
    req = requests.get(url, headers=headers,  params=query_string)

    if req.status_code != 200:
        print(None)
        return 0
    data = req.json()
    top_level = data.get("data").get("children")
    after = data.get("data").get("after")
    for hot_post in top_level:
        titile = hot_post.get("data").get("title")
        hot_list.append(titile)
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
