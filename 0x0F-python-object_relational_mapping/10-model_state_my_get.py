#!/usr/bin/python3
"""Script that retrieves and prints the ID of a specific State object from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    '''Check if the correct number of command-line arguments is provided'''
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    '''Get command-line arguments'''
    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    '''Create a database connection'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    '''Create a session'''
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        '''Query the State object with the specified name'''
        state = session.query(State).filter_by(name=state_name).first()

        if state:
            print(state.id)
        else:
            print("Not found")

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

    finally:
        # Close the session
        session.close()
