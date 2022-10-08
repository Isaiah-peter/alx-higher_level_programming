#!/usr/bin/python3

import MySQLdb
"""module mysqlLdb"""

import sys
"""gets the argv"""

db = MySQLdb.connect(host=sys.argv[1], user=sys.argv[2], db=sys.argv[3])

cur = db.cursor()
cur.execute("SELECT * FROM states")
rows = cur.fetchall()
for row in rows:
  print(f"({row.id}, {row.name})")