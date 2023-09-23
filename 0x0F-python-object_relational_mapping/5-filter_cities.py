#!/usr/bin/python3
"""
Script that lists all cities from the database
"""

import MySQLdb
import sys

if __name__ == '__main__':
    '''
    Create a database connection
    '''
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    '''Create a cursor'''
    cur = db.cursor()

    '''Execute the SQL query to retrieve city names'''
    cur.execute("SELECT cities.name FROM cities\
                 JOIN states ON cities.state_id = states.id\
                 WHERE states.name = %s ORDER BY cities.id",
                (sys.argv[4],))

    '''Fetch all the rows'''
    rows = cur.fetchall()

    '''Extract city names into a list'''
    city_names = [row[0] for row in rows]

    '''Join city names with ", " separator'''
    result = ", ".join(city_names)
    Print the result
    print(result)
    cur.close()
    db.close()
