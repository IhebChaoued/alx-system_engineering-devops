#!/usr/bin/python3
""" API Subs """
import requests


def number_of_subscribers(subreddit):
    """ Reddit API """
    link = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'ALX aAPI task 0'}
    resp = requests.get(link, headers=headers, allow_redirects=False)

    if resp.status_code == 200:
        return resp.json()['data']["subscribers"]
    else:
        return 0
