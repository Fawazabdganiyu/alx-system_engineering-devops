#!/usr/bin/python3
""" Query the Reddit API and returns the number of subscribers
"""


def number_of_subscribers(subreddit):
    """ Get the numbers of subscribers in the given subreddit
    """
    import requests

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get('data').get('subscribers')

    return 0
