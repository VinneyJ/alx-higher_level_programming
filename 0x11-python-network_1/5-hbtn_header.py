#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    arg1 = sys.argv[1]
    req = requests.get(arg1)
    print(req.headers.get("X-Request-Id"))
