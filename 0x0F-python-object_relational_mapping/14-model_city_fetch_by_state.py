#!/usr/bin/python3
"""
Script that Lists all City objects from the database
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    '''Create a database connection using SQLAlchemy'''
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    '''Create a session to interact with the database'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''
    Query City and State objects, filtering and ordering as needed
    '''
    for city, state in session.query(City, State) \
                              .filter(City.state_id == State.id) \
                              .order_by(City.id):
        '''Print the desired information'''
        print("{}: ({}) {}".format(state.name, city.id, city.name))
