#!/usr/bin/python3
from urllib.error import HTTPError
import urllib.request
import sys

""" takes in a URL, sends a request to the URL and displays the body of the response"""
if __name__ == "__main__":
    arg1 = sys.argv[1]
    try:
        with urllib.request.urlopen(arg1) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
