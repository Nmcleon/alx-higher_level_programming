#!/usr/bin/python3
"""
Script lists all states with a name starting with N
from the database hbtn_0e_0_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        db = MySQLdb.connect(
                host="localhost",
                passwd=password,
                db=database
                )
        cur = db.cursor()
        cur.execute(
                "SELECT * FROM states "
                "WHERE name LIKE BINARY 'N%' "
                "ORDER BY id"
                )
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
