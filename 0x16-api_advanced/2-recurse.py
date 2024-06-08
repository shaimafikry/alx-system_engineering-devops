#!/usr/bin/python3
"""func to get the top 10 titles"""
import requests


def recurse(subreddit, hot_list=[]):
    """func to get the top 10 titles"""
    # end point url
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Myscript/1.0 (0-subs)"}
    data = requests.get(url, headers=headers)
    if (data.status_code == 200):
        content = data.json()
        comments = content["data"]["children"]
        for comment in comments:
            hot_list.append(comment["data"]["title"])
        return (hot_list)
    else:
        return None
