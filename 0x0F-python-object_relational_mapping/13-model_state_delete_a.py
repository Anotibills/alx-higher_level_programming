#!/usr/bin/python3
"""
Script that deletes State objects with names containing the letter 'a'
"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    '''
    Check if the correct number of command-line arguments is provided
    '''
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    '''
    Get command-line arguments
    '''
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create a database connection
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    '''Create a session'''
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        '''
        Query State objects with names containing 'a'
        '''
        states_with_a = session.query(State).filter(State.name.like('%a%')).all()
        '''
        Delete the matching State objects
        '''
        for state in states_with_a:
            session.delete(state)
        '''
        Commit the changes to the database
        '''
        session.commit()

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

    finally:
        # Close the session
        session.close()
