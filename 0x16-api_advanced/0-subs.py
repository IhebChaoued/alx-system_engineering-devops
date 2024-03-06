#!/usr/bin/python3
""" Subs """

import requests


def number_of_subscribers(subreddit):
    """ Reddit API """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = {"User-Agent": "custom-user-agent"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    elif response.status_code == 404:
        return 0
    else:
        return 0
