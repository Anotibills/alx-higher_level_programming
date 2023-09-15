#!/usr/bin/python3
"""Script that takes in the name of a state as an argument
and lists all cities from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    '''Check if the correct number of command-line arguments is provided'''
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    '''Get command-line arguments'''
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

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

        '''Execute the query to grab cities from the specified state'''
        cur.execute("SELECT cities.name FROM cities "
                    "LEFT OUTER JOIN states ON cities.state_id = states.id "
                    "WHERE states.name = %s;", (state_name,))

        '''Fetch all the rows'''
        query_rows = cur.fetchall()

        '''Create a list to store city names'''
        city_names = [row[0] for row in query_rows]

        '''Print the results'''
        if city_names:
            print(', '.join(city_names))
        else:
            print("No cities found for state: {}".format(state_name))

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
        sys.exit(1)

    finally:
        '''Close the cursor and the database connection'''
        if cur:
            cur.close()
        if db:
            db.close()
