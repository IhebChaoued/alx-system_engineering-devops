#!/usr/bin/python3
""" API Sub """
import requests


def top_ten(subreddit):
    """ Hot 10 posts """
    link = f'https://www.reddit.com/r/{subreddit}/hot.json?show="all"&limit=10'
    headers = {'User-Agent': 'ALX aAPI task 1'}
    resp = requests.get(link, headers=headers, allow_redirects=False)

    if resp.status_code >= 300:
        return 0

    for post in resp.json()["data"]["children"]:
        print(post["data"]["title"])
