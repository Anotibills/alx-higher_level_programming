#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument
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

    '''Create a session'''
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Get the state name from command-line arguments
        state_name = sys.argv[4]
        '''
        Query and print the State object with the specified name
        '''
        state = session.query(State).filter_by(name=state_name).first()
        if state:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("    {}: {}".format(city.id, city.name))
        else:
            print("State not found")

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

    finally:
        # Close the session
        session.close()
