#!/usr/bin/python3
"""Function to get a list of  hot posts on a  subreddit."""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursively retrieves a list of the titles of all hot articles for a given
    subreddit.

    Args:
        subreddit (str): The name of the subreddit to retrieve hot articles
        from.
        hot_list (list): A list to store the titles of the hot articles.
        after (str): A token identifying the next page of results to retrieve.
        count (int): The number of results already retrieved.

    Returns:
        A list of the titles of all hot articles for the given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=header, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
