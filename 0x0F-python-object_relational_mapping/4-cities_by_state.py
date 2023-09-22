#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <usernaem> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    '''Get command-line argument'''
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        '''Connect the database'''
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
            )

        '''Create a cursor object'''
        cur = db.cursor()
        '''Execute query to grab all cities'''
        cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                    "JOIN states ON cities.state_id = states.id "
                    "ORDER BY cities.id ASC")

        query_rows = cur.fetchall()

        '''Print the results'''
        for row in query_rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

    finally:
        '''Close the cursor and the database connection'''
        if cur:
            cur.close()
        if db:
            db.close()
