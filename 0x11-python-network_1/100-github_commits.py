#!/usr/bin/python3
""" Script that lists most recent 10 commits on
Github repo"""


import requests
from sys import argv
if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits"\
            .format(argv[1], argv[2])

    req = requests.get(url).json()

    try:
        for x in range(10):
            print("{}: {}".format(req[x]
                  .get('sha'), req[x].get('commit').get('author').get('name')))

    except Exception:
        pass
