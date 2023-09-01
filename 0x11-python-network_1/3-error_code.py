#!/usr/bin/python3
"""
Sends a request to a given URL and displays the response body.

Usage: ./send_request.py <URL>
"""

import sys
import urllib.error
import urllib.request


if __name__ == "__main__":
    # Get the URL from command-line arguments
    url = sys.argv[1]

    try:
        # Send the request and display the response body
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode("utf-8")
            print(response_body)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors by printing the error code
        print("Error code:", e.code)
