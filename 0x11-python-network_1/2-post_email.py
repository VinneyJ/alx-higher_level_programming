import urllib.request
import urllib.parse
import sys

""" Takes an email sends a post """
if __name__ == "__main__":
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    values = {}
    values["email"] = arg2

    data = urllib.parse.urlencode(values)
    data = data.encode("utf-8")
    req = urllib.request.Request(arg1, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
