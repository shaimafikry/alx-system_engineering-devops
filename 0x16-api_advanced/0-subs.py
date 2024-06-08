#!/usr/bin/python3
"""func to get the num of suscribers of a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """func to get the num of suscribers of a given subreddit"""
    # end point url
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    data = requests.get(url)
    if (data.status_code == 200):
        content = data.json()
        extract_content = content["data"]
        num = extract_content.get("subscribers")
        # print (num)
        return num
    else:
        return 0
