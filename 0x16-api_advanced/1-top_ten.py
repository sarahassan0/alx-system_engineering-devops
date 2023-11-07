#!/usr/bin/python3
"""Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit."""

import requests


def top_ten(subreddit):
    """gets the titles of the first 10 hot posts"""

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(
        subreddit)
    res = requests.get(url, headers={'User-Agent': 'anything'},
                       allow_redirects=False)

    if res.status_code == 200:
        posts = res.json().get('data', {}).get('children', [])
        for post in posts:
            print(post.get('data', {}).get('title', ''))
    else:
        print(None)
