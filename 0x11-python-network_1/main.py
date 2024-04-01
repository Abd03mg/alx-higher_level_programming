#!/usr/bin/python3 

import requests
from sys import argv

req = requests.get('https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])).json()


print("Len: {}\ntype: {}\n\nreq: {}".format(len(req), type(req), req[0]))
