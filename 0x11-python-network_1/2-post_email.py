#!/usr/bin/python3
""" Python script that gets email variable"""


if __name__ == "__main__":
    from sys import argv
    from urllib import request, parse

    data = parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as res:
        con = res.read()
        print(con.decode("utf-8"))
