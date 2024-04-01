#!/usr/bin/python3
""" python script that sends request to URL
    and displays body. """

from urllib import request, parse
import urllib.error
from sys import argv

if __name__ == "__main__":
    req = request.Request(argv[1])

    try:
        with request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
