#!/usr/bin/python3
"""POST an email #1"""

from sys import argv
import requests

if __name__ == "__main__":
    data = {'email': argv[2]}
    response = requests.post(argv[1], data)
            print(response.text)
