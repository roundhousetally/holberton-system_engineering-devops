#!/usr/bin/python3
""" getting subs from reddit """
import requests


def top_ten(subreddit):
    """ queries reddit for top ten of a subreddit """
    usr = {'User-Agent': 'NicCage'}
    url = "https://www.reddit.com/r/{}/hot/.json?limit=10".format(subreddit)
    req = requests.get(url, headers=usr, allow_redirects=False).json()
    try:
        list = req.get('data').get('children')
        for r in list:
            print(r.get('data').get('title'))

    except Exception:
        print(None)
