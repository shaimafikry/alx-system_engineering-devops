#!/usr/bin/python3
"""func to get the num of suscribers of a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """func to get the num of suscribers of a given subreddit"""
    # end point url
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "shaimaa"}
    data = requests.get(url, headers=headers)
    if (data.status_code == 200):
        content = data.json()
        num = content["data"]["subscribers"]
        # print (num)
        return num
    else:
        return 0
