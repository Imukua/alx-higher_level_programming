#!/usr/bin/python3
"""
Sends a POST request to a specified URL with an email parameter.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    # Get the URL and email from command-line arguments
    target_url = sys.argv[1]
    email_value = {"email": sys.argv[2]}

    # Encode the email parameter as ASCII
    encoded_data = urllib.parse.urlencode(email_value).encode("ascii")

    # Create a POST request with the encoded data
    request = urllib.request.Request(target_url, encoded_data)

    # Send the request and print the response body
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode("utf-8")
        print(response_body)
