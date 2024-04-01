#!/usr/bin/python3
""" Python script that Uses
'request' module to get X-Request-Id value."""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get(argv[1])
    print(r.headers.get("X-Request-Id"))
