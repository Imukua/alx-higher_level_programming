#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter as a
parameter and processes the response.
"""

import sys
import requests

if __name__ == "__main__":
    # Get the letter from command-line arguments, set q="" if not provided
    letter = sys.argv[1] if len(sys.argv) > 1 else ""

    # Define the URL
    url = "http://0.0.0.0:5000/search_user"

    # Create a data dictionary with the letter parameter
    data = {"q": letter}

    try:
        # Send a POST request with the data
        response = requests.post(url, data=data)

        # Check if the response is valid JSON and not empty
        try:
            result = response.json()
            if result:
                print("[{}] {}".format(result.get("id"), result.get("name")))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print("Error:", e)
