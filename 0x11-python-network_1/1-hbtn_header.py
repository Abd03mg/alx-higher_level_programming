#!/usr/bin/python3
""" Python script that gets header X-Request-Id."""


if __name__ == "__main__":
    from sys import argv
    from urllib import request

    req = request.Request(argv[1])
    with request.urlopen(req) as res:
        con = dict(res.headers).get("X-Request-Id")
        print(con)
