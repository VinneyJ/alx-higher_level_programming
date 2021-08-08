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
    cur.execute("SELECT cities.id, cities.name, states.name\
    FROM cities JOIN states ON cities.state_id = states.id ORDER BY id ASC")
    states = cur.fetchall()

    trigger = 0
    for state in states:
        if state[2] == sys.argv[4]:
            print("{:s}".format(state[1]), end="")
            if trigger < len(state) - 1:
                print(", ", end="")
                trigger += 1
    print("")
    cur.close()
    conn.close()
