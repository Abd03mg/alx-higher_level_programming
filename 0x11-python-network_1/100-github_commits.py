#!/usr/bin/python3
""" Script that lists most recent 10 commits on
Github repo"""


import requests
from sys import argv
if __name__ == '__main__':
    url = "https://api.github.com/repos/{}/{}/commits"\
            .format(argv[2], argv[1])

    req = requests.get(url).json()
    lim = 10 if len(req) > 10 else len(req)
    for x in range(lim):
        print("{}: {}".format(req[x]
              .get('sha'), req[x].get('commit').get('author').get('name')))
