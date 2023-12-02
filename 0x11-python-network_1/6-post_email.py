#!/usr/bin/python3
"""POST an email #1"""

from requests import post
from sys import argv

if __name__ == "__main__":
    html = post(argv[1]
    data={'email': argv[2]})
    print(html.text)
