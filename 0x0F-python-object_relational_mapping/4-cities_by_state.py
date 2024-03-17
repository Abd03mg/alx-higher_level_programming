#!/usr/bin/python3
""" Script that lists all 'states' from database 'hbtn...'"""


import MySQLdb
from sys import argv as arg

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", user=arg[1], passwd=arg[2], db=arg[3])
    cur = db.cursor()
    cur.execute(
        "SELECT \
            c.id, c.name, s.name \
        FROM \
            cities as c INNER JOIN states as s ON c.state_id = s.id \
        ORDER BY \
            c.id ASC")
    for i in cur.fetchall():
        print(i)
