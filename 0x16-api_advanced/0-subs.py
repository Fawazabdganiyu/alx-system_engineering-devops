#!/usr/bin/python3
"""
Query the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Get the numbers of subscribers in the given subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/abu_Fawzaan)'
    }
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json()
        return data['data']['subscribers']

    return 0
