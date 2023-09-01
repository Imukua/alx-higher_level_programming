#!/usr/bin/python3
"""
Sends a POST request to a given URL with an email as a parameter
and displays the response body.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()

        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
