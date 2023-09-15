#!/usr/bin/python3
"""script that lists all cities in a specific state from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == "__main__":
    '''
    Check if the correct number of command-line arguments is provided
    '''
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    # Get command-line arguments
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    '''
    Create a database connection
    '''
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
    cur = db.cursor()

    try:
        '''
        Query and print the names of cities in the specified state
        '''
        cur.execute("""SELECT cities.name FROM
                    cities INNER JOIN states ON states.id=cities.state_id
                    WHERE states.name=%s""", (state_name,))
        rows = cur.fetchall()
        city_names = [row[0] for row in rows]
        print(", ".join(city_names))

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

    finally:
        # Close the cursor and database connection
        cur.close()
        db.close()
