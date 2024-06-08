#!/usr/bin/python3
"""func to get the top 10 comments"""
import requests


def top_ten(subreddit):
    """func to get the top 10 comments"""
    # end point url
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Myscript/1.0 (0-subs)"}
    data = requests.get(url, headers=headers)
    if (data.status_code == 200):
        content = data.json()
        comments = content["data"]["children"]
        i = 1
        for comment in comments:
            print(comment["data"]["title"])
            i = i + 1
            if i == 10:
                return
    else:
        return None
