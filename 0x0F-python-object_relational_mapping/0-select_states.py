#!/usr/bin/python3
""" Script that lists all 'states' from database 'hbtn...'"""


import MySQLdb
from sys import argv as arg

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost", user=arg[1], passwd=arg[2], db=arg[3])
    cur = db.cursor()
    cur.excecute("SELECT * FROM htbn_0e_usa")
    for i in cur.fetchall():
        print(i)
