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
    headers = {'User-Agent': 'My Custom Agent/1.0'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    posts = response.json().get('data').get('children')
    for post in posts:
        print(post.get('data').get('title'))
