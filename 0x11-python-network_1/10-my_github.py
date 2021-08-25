#!/usr/bin/python3
"""
takes your GitHub credentials
(username and password) and uses
the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    import sys

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    url = "https://api.github.com/user"
    try:
        req = requests.get(url, auth=(arg1, arg2))
        print(req.json()["id"])
    except:
        print("None")
