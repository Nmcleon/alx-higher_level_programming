#!/usr/bin/python3
""" Error code #0 """

from urllib import request, parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    header = parse.urlencode(value).encode()
    with request.urlopen(request.Request(url, header)) as response:
        print(response.read().decode("utf-8"))
