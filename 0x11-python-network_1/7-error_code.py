#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    arg1 = sys.argv[1]
    req = requests.get(arg1)
    if int(req.status_code) >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
