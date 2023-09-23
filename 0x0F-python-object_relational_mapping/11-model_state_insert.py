#!/usr/bin/python3
"""
Script that uses SQLAlchemy to insert a new State object into a database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    '''
    Check if the correct number of command-line arguments is provided
    '''
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>"
              .format(sys.argv[0]))
        sys.exit(1)

    '''
    Get command-line arguments for username, password, and database name
    '''
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    '''
    Create a database connection using SQLAlchemy
    '''
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, database))

    '''Create the database schema if it doesn't exist'''
    Base.metadata.create_all(bind=engine)

    '''Create a session to interact with the database'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Create a new State object and add it to the session'''
    new_state = State(name="Louisiana")
    session.add(new_state)

    '''Commit the changes to the database'''
    session.commit()

    '''Print the ID of the newly inserted State object'''
    print("{}".format(new_state.id))
    session.close()
