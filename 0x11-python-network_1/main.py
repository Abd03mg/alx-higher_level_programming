#!/usr/bin/python3 

import requests
from sys import argv

req = requests.get('https://api.github.com/repos/{}/{}/commits'.format(argv[1], argv[2])).json()


print("Len: {}\ntype: {}\n\nreq: {}\n\n".format(len(req), type(req), ''))
#for i in req:
print(req[0]['commit'])
print(req[0].keys())

