#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
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

    '''Query all City objects and order them by ID'''
    for city in session.query(City).order_by(City.id):
        '''
        Print the city's information and its corresponding state's name
        '''
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
