#!/usr/bin/python3

""" It fetches Url """
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    print("\t- {}".format(response.read()))
