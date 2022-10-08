#!/usr/bin/python3
"""
select cities id name and state name of the cities
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                     user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()

    cur.execute("""SELECT c.id, c.name, s.name FROM cities as c
                JOIN states as s ON
                s.id = c.state_id
                ORDER BY c.id, s.name""")
    rows = cur.fetchall()

    for row in rows:
        print(f"{row}")