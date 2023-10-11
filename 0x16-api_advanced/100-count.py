#!/usr/bin/python3
"""Defines a function to count words in hot posts of a subreddit."""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """
    Count the number of occurrences of words in a subreddit's titles.

    Args:
        subreddit (str): The name of the subreddit to search.
        word_list (list): A list of words to search for in the subreddit's
        titles.
        instances (dict): A dictionary to store the number of occurrences
        of each word.
        after (str): A token to indicate the starting point of the next page
        of results.
        count (int): The total number of results counted so far.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    header = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by Imukua)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=header, params=params,
                            allow_redirects=False)
    try:
        results = response.json()
        if response.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for f in results.get("children"):
        title = f.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                times = len([tl for tl in title if tl == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
