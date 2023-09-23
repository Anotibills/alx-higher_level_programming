#!/usr/bin/python3
"""
Script that lists all States and corresponding Cities in database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    '''Create a SQLAlchemy engine for the specified database'''
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    '''Create a session to interact with the database'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''Query all State objects and order them by ID'''
    for state in session.query(State).order_by(State.id):
        # Print the state's information
        print("{}: {}".format(state.id, state.name))

        '''Iterate through the state's cities and print their information'''
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
