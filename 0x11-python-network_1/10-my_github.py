#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    url = "https://api.github.com/user"
    try:
        req = requests.get(url, auth=(arg1, arg2))
        print(req.json()["id"])
    except:
        print("None")
