#!/usr/bin/python3
"""
Script that prints the City objects associated with the State name passed as an argument
"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    '''
    Check if the correct number of command-line arguments is provided
    '''
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    '''
    Create a database connection
    '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database))
    '''
    Create a session
    '''
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        '''Get the state name'''
        state_name = sys.argv[4]
        '''
        Query and print City objects associated with the specified state name
        '''
        for city in session.query(City).join(State).filter(State.name == state_name):
            print("{}: {} -> {}".format(city.id, city.name, state_name))

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

    finally:
        # Close the session
        session.close()
