#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter
and displays the response body.

Usage: ./send_post_request.py <URL> <email>
"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary with the email parameter
    data = {"email": email}

    # Encode the data as ASCII
    encoded_data = urllib.parse.urlencode(data).encode("ascii")

    # Create a POST request with the encoded data
    request = urllib.request.Request(url, encoded_data)

    # Send the request and display the response body
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
        print(response_body)
