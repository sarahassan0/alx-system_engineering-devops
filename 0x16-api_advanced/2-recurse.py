#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of all
    hot posts listed for a given subreddit."""

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Queries the Reddit API and returns a list containing the titles
        of all hot articles for a given subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json?limit=100'.format(
        subreddit)
    params = {
        'after': after,
        'count': count
    }
    res = requests.get(url, headers={'User-Agent': 'anything'}, params=params,
                       allow_redirects=False)

    if res.status_code == 200:
        data = res.json().get('data', {})
        posts = data.get('children', [])
        for post in posts:
            hot_list.append(post.get('data', {}).get('title', ''))

        after = data.get('after', None)
        count = len(hot_list[1:])
        if after:
            return recurse(subreddit, hot_list, after, count)
        else:
            return hot_list
