#!/usr/bin/python3
'''Defines a function to print hot posts for a subredit'''
import requests


def top_ten(subreddit):
    """
    Returns the top 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve posts from.

    Returns:
        None if the subreddit is not found, otherwise prints the titles of
        the top 10 hot posts.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    parameters = {
        "limit": 10
    }
    response = requests.get(url, headers=header, params=parameters,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
