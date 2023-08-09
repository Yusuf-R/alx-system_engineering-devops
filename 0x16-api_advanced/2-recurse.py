#!/usr/bin/python3
"""Using recursion to get all the hot posts for a subreddit"""
import requests


def recurse(subreddit, hot_list=[], nxt_lnk=None):
    """
    This function queries the Reddit API and
    prints the titles of ALL the hot posts listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = headers = {"User-Agent": "Mozilla/5.0"}
    query_string = {"after": nxt_lnk}
    req = requests.get(
        url, headers=headers, allow_redirects=False, params=query_string
    )

    if req.status_code != 200:
        print(None)
        return 0
    data = req.json()
    nxt_lnk = data.get("data").get("after")
    top_level = data.get("data").get("children")
    for hot_topics in top_level:
        title = hot_topics.get("data").get("title")
        hot_list.append(title)
    if nxt_lnk is not None:
        recurse(subreddit, hot_list, nxt_lnk)
    return hot_list
