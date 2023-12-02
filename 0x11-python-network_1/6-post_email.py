#!/usr/bin/python3
"""POST an email #1"""

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    response = post(url, data=email)
            print(response.text)
