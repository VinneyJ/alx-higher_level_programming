#!/usr/bin/python3
"""

a script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa,
where name matches the argument.
this time, safe from SQL injection.
"""


import sys
import MySQLdb


if __name__ == "__main__":
    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], host="localhost",
                           port=3306)
    # Connect it to cursor
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    states = cur.fetchall()

    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
    # print("Item is not available")
    cur.close()
    conn.close()
