#!/usr/bin/python3
"""
Script that lists all cities of a state from
the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )
        cur = db.cursor()
        num_rows = cur.execute("SELECT cities.name FROM cities WHERE state_id =\
                (SELECT id FROM states WHERE name LIKE BINARY %s)\
                ORDER BY cities.id;", (state_name, ))
        row = cur.fetchone()
        i = 1
        for row in orws:
            print(row[0], end='')
            if i < num_rows:
                print(end=', ')
            i += 1
        print()
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
