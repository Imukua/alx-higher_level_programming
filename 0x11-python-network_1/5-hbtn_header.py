#!/usr/bin/python3
"""
Sends a request to a given URL and displays the value of the X-Request-Id header.
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        response = requests.get(url)
        response.raise_for_status()

        x_request_id = response.headers.get('X-Request-Id')

        if x_request_id:
            print(x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
