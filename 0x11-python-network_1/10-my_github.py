#!/usr/bin/python3
"""
Lists the 10 most recent commits from a GitHub repository.

Usage: ./list_commits.py <repository_name> <owner_name>
"""

import sys
import requests

if __name__ == "__main__":
    # Get the repository name and owner name from command-line arguments
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Define the GitHub API URL for listing commits
    api_url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

    try:
        # Send a GET request to the GitHub API
        response = requests.get(api_url)

        # Check if the request was successful
        if response.status_code == 200:
            commits_data = response.json()

            # List the 10 most recent commits
            for commit in commits_data[:10]:
                sha = commit.get("sha")
                author_name = commit.get("commit").get("author").get("name")
                print(f"{sha}: {author_name}")
        else:
            pass
    except requests.exceptions.RequestException as e:
        print("Error:", e)
