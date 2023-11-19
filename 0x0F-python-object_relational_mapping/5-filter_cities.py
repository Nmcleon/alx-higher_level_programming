#!/usr/bin/python3
"""
Script that lists all cities of a state from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} username password databas_name".format(sys.argv[0]))
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
        cur.execute("""SELECT cities.name FROM
                    cities INNER JOIN states ON states.id=cities.state_id
                    WHERE states.name=%s""", (sys.argv[4],))          
        rows = cur.fetchall()
        tmp = list(row[0] for row in rows)
        print(*tmp, sep=", ")
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)
