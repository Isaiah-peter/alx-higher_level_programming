#!/usr/bin/python3

import MySQLdb
from sys import argv

db = MySQLdb.connect(host="localhost", port=3306,
                     user=argv[1], passwd=argv[2], db=argv[3])
cur = db.cursor()

cur.execute("SELECT id, name FROM states")
rows = cur.fetchall()
for row in rows:
    if row[1][0] == "N":
        print(f"{row}")

cur.close()
db.close()
