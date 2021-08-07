#!/usr/bin/python3
import sys
import MySQLdb


"""
    Initializes the arguments, connects and closes the database.
"""
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
conn = MySQLdb.connect(user=arg1, passwd=arg2, db=arg3, charset="utf8")
cur = conn.cursor()
# HERE I have to know SQL to grab all states in my database
cur.execute("SELECT * FROM states ORDER BY id ASC")

query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
