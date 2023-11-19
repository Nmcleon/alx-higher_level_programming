#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(sys.argv[0]))
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            passwd=password,
            db=database
        )
        cur = db.cursor()
        num_rows = cur.execute("SELECT * FROM states WHERE states.name LIKE BINARY\
                               '{}' ORDER BY states.id;".format(state_name))
        
        rows = cur.fetchall()
        for row in rows:
            print(row)

        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
