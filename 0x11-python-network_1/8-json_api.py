#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    arg1 = str(sys.argv[1])
    data = {"q": ""}
    if len(sys.argv) < 1:
        print("No result")
    else:
        data["q"] = arg1
        req = requests.post(url, data=data)
        try:
            print("[{:d}] {}".format(req.json()["id"], req.json()["name"]))
        except Exception:
            print("Not a valid JSON")
