#!/usr/bin/python3
"""
Query the Reddit API, parse the the title of all hot articles,
and print a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript,
but java should not).
"""
import requests


def count_words(subreddit, word_list):
    """ Count words """
