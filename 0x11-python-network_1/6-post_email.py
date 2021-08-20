!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    data = {}
    data["email"] = arg2
    req = requests.post(arg1, data=data)
    print(req.text)
