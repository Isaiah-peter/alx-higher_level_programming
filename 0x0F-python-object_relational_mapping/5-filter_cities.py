#!/usr/bin/python3
"""
select cities name where state == %(name)s {name:argv[4]}
"""

from operator import le
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                     user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()

    cur.execute("""SELECT c.name FROM cities as c
                JOIN states as s ON
                s.id = c.state_id
                WHERE s.name = %(name)s
                ORDER BY c.id""", {"name": argv[4]})
    rows = cur.fetchall()

    count = 0
    while len(rows) > count:
        if count != len(rows) - 1:
            print(f"{rows[count][0]}", end=", ")
        else:
            print(f"{rows[count][0]}")

        count += 1

    if count == 0:
        print("")