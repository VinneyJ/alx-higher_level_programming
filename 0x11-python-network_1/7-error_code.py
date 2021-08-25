#!/usr/bin/python3
"""
script that takes in a URL,
sends a request to the URL and displays
the body of the response.
"""


if __name__ == "__main__":
    import requests
    import sys

    arg1 = sys.argv[1]
    req = requests.get(arg1)
    if int(req.status_code) >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)
