#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the body of the response"""


if __name__ == "__main__":
    import sys
    import urllib.request
    from urllib.error import HTTPError

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8", "replace"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
