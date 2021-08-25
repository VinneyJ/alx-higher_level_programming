#!/usr/bin/python3
"""
takes in a URL and an email address,
sends a POST request to the passed URL with
the email as a parameter, and finally displays
the body of the response.
"""


if __name__ == "__main__":
    import requests
    import sys

    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    data = {}
    data["email"] = arg2
    req = requests.post(arg1, data=data)
    print(req.text)
