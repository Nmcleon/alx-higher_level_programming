#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username database password".format(sys.argv[0]))
        sys.exit(1)

        username = sys.argv[1]
        database = sys.argv[2]
        password = sys.argv[2]

        try:
            db = MySQLdb.connect(
                    host="localhost",
                    port=3306,
                    user=username,
                    passwd=password,
                    db=database
                    )
            cur = db.cursor()
            cur.execute("SELECT * FROM states ORDER BY id")
            for state in cur.fetchall():
                print(state)
                cur.close()
                db.close()
        except MySQLdb.Error as e:
            print("MySQL Error:", e)
            sys.exit(1)
