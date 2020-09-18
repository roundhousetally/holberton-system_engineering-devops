#!/usr/bin/python3
""" getting subs from reddit """
import requests


def number_of_subscribers(subreddit):
    """ queries reddit for subs """
    usr = {'User-Agent': 'NicCage'}
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers=usr, allow_redirects=False).json()
    try:
        return req.get('data').get('subscribers')
    except Exception:
        return 0
