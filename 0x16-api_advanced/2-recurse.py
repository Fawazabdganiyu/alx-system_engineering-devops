#!/usr/bin/python3
"""
Query the Reddit API and return a list containing the titles of all hot articles
for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Get the list containing the titles of all hot articles of a subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'My Custom Agent/1.0'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    posts = response.json().get('data').get('children')
    for post in posts:
        hot_list.append(post.get('data').get('title'))
    after = response.json().get('data').get('after')
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
