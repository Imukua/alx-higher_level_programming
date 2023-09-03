# alx-higher_level_programming README

This repository contains Python scripts for various network-related tasks as part of the ALX Higher Level Programming curriculum. Each script is designed to perform specific tasks related to network requests, handling HTTP responses, and working with APIs.

## Table of Contents

1. [0-hbtn_status.py](#0-hbtn_statuspy)
2. [1-hbtn_header.py](#1-hbtn_headerpy)
3. [2-post_email.py](#2-post_emailpy)
4. [3-error_code.py](#3-error_codepy)
5. [4-hbtn_status.py](#4-hbtn_statuspy)
6. [5-hbtn_header.py](#5-hbtn_headerpy)
7. [6-post_email.py](#6-post_emailpy)
8. [7-error_code.py](#7-error_codepy)
9. [8-json_api.py](#8-json_apipy)
10. [10-my_github.py](#10-my_githubpy)
11. [100-github_commits.py](#100-github_commitspy)

## 0-hbtn_status.py

This script fetches the [https://alx-intranet.hbtn.io/status](https://alx-intranet.hbtn.io/status) URL using the `urllib` package and displays the response's body, content type, and UTF-8 content.

Usage:
```bash
$ ./0-hbtn_status.py | cat -e
```

## 1-hbtn_header.py

This script takes a URL as input, sends a request to the URL using `urllib`, and displays the value of the X-Request-Id variable found in the response header.

Usage:
```bash
$ ./1-hbtn_header.py https://alx-intranet.hbtn.io
```

## 2-post_email.py

This script takes a URL and an email as input, sends a POST request to the URL with the email as a parameter, and displays the body of the response (decoded in UTF-8).

Usage:
```bash
$ ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
```

## 3-error_code.py

This script takes a URL as input, sends a request to the URL using `urllib`, and displays the body of the response (decoded in UTF-8). It also handles `urllib.error.HTTPError` exceptions and prints the error code if the HTTP status code is greater than or equal to 400.

Usage:
```bash
$ ./3-error_code.py http://0.0.0.0:5000
$ ./3-error_code.py http://0.0.0.0:5000/status_401
$ ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
$ ./3-error_code.py http://0.0.0.0:5000/status_500
```

## 4-hbtn_status.py

This script fetches the [https://alx-intranet.hbtn.io/status](https://alx-intranet.hbtn.io/status) URL using the `requests` package and displays the response's body, content type, and UTF-8 content.

Usage:
```bash
$ ./4-hbtn_status.py | cat -e
```

## 5-hbtn_header.py

This script takes a URL as input, sends a request to the URL using `requests`, and displays the value of the X-Request-Id variable in the response header.

Usage:
```bash
$ ./5-hbtn_header.py https://alx-intranet.hbtn.io
```

## 6-post_email.py

This script takes a URL and an email as input, sends a POST request to the URL with the email as a parameter using `requests`, and displays the body of the response (decoded in UTF-8).

Usage:
```bash
$ ./6-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
```

## 7-error_code.py

This script takes a URL as input, sends a request to the URL using `requests`, and displays the body of the response. If the HTTP status code is greater than or equal to 400, it prints the error code.

Usage:
```bash
$ ./7-error_code.py http://0.0.0.0:5000
$ ./7-error_code.py http://0.0.0.0:5000/status_401
$ ./7-error_code.py http://0.0.0.0:5000/doesnt_exist
$ ./7-error_code.py http://0.0.0.0:5000/status_500
```

## 8-json_api.py

This script takes a letter as input, sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter, and displays the response. It handles JSON formatting and empty responses.

Usage:
```bash
$ ./8-json_api.py
$ ./8-json_api.py a
$ ./8-json_api.py 2
$ ./8-json_api.py b
```

## 10-my_github.py

This script takes GitHub credentials (username and personal access token) and uses the GitHub API to display the user's ID. It uses Basic Authentication with the personal access token.

Usage:
```bash
$ ./10-my_github.py username personal_access_token
```

## 100-github_commits.py

This advanced script takes a repository name and owner name as input, and uses the GitHub API to list the 10 most recent commits of the specified repository by the given owner. It prints each commit's SHA and author name.

Usage:
```bash
$ ./100-github_commits.py repository_name owner_name
```

