#!/usr/bin/python3
""" Error code #0 """

if __name__ == "__main__":
from urllib.request import urlopen
from urllib.err import HTTPError
from sys import argv
    
    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as error:
        print(f'Error code: {error.status}')
