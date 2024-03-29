#!/usr/bin/python3
"""
fetch all state stating from N
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                     user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()

    cur.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(f"{row}")

    cur.close()
    db.close()
