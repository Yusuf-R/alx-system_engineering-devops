#!/usr/bin/property
"""using recursion to make an API call"""
import requests


def count_words(subreddit, word_list, dict_cnt=None, nxt_pg=None):
    """use recursion to query our API"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    q_string = {"after": nxt_pg}
    data = (requests.get(url, headers=headers,
                         params=q_string,
                         allow_redirects=False))

    if data.status_code != 200:
        print(None)
        return

    if dict_cnt is None:
        dict_cnt = {}

    data_json = data.json()
    top_lvl = data_json.get("data").get("children")
    nxt_pg = data_json.get("data").get("after")

    for i in top_lvl:
        title = i.get("data").get("title")
        for lang in word_list:
            dict_cnt[lang.lower()] = (dict_cnt.get(lang.lower(), 0) +
                                      title.lower().split().
                                      count(lang.lower()))
    if nxt_pg:
        count_words(subreddit, word_list, dict_cnt, nxt_pg)
    # sort descending order >>--- highest to lowest >>>---
    dict_sort = (dict(sorted(dict_cnt.items(),
                             key=lambda x: x[1],
                             reverse=True)))
    rt_dict = {}
    for k, v in dict_sort.items():
        if v == 0:
            continue
        rt_dict[k] = v
    return (rt_dict)
