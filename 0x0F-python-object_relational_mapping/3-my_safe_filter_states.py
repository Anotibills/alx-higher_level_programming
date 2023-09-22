#!/usr/bin/python3
"""A script that lists all states from the database hbtn_0e_0_usa
with a specified name"""

import MySQLdb
import sys

if __name__ == '__main__':
    '''Check if the correct number of command-line arguments is provided'''
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    '''Get command-line arguments'''
    username, password, database, state_name = (
            sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

    try:
        '''Connect to the database'''
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

        '''Execute the query to grab states with the specified name'''
        cur.execute("SELECT * FROM states WHERE name = %s;", (state_name,))

        '''Fetch all the rows'''
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
