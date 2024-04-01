#!/usr/bin/python3
""" Script that lists most recent 10 commits on
Github repo"""


if __name__ == '__main__':
    import requests
    from sys import argv

    req = requests.get(
            'https://api.github.com/repos/{}/{}/commits'
            .format(argv[1], argv[2])).json()

    try:
        for x in range(0, 10):
            print("{}: {}".format(req[x]
                  .get('sha'), req[x].get('commit').get('author').get('name')))

    except IndexError:
        print('', end='')
