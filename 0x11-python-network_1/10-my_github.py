#!/usr/bin/python3
"""Script that uses REST API to get user ID."""

if __name__ == '__main__':
    from sys import argv
    import requests

    req = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))
    print(req.json().get('id'))
