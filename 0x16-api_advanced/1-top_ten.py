#!/usr/bin/python3
"""
Query the Reddit API and print the top 10 hot posts for a subreddit
"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the top 10 hot posts for a subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'linux:0x16.api.advanced:v1.0.0 (by /u/abu_Fawzaan)'
    }
    params = {'limit': 10}
    r = requests.get(url, headers=headers, params=params,
                     allow_redirects=False)
    if r.status_code != 200:
        print(None)
        return
    else:
        posts = r.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
