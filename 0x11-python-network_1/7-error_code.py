#!/usr/bin/python3
"""
Sends a request to a given URL and displays the response body
or handles HTTP errors.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)

        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
