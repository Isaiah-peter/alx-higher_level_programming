#!/usr/bin/python3

import MySQLdb
"""module mysqlLdb"""

import sys
"""gets the argv"""

db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

cur = db.cursor()
cur.execute("SELECT id, name FROM states ORDER BY id")
rows = cur.fetchall()
for row in rows:
  print(f"{row}")