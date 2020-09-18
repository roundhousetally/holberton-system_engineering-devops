#!/usr/bin/python3
""" getting subs from reddit """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ queries reddit for top ten of a subreddit """
    usr = {'User-Agent': 'NicCage'}
    url = "https://www.reddit.com/r/{}/hot/.json?after={:}".format(
        subreddit, after)
    req = requests.get(url, headers=usr, allow_redirects=False).json()
    try:
        list = req.get('data').get('children')
        for r in list:
            r_dict = r.get('data')
            hot_list.append(r_dict.get('title'))
        after = req.get('data').get('after')
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)

    except Exception:
        return None
