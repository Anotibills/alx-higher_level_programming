#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco"
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    '''Create a SQLAlchemy engine for the specified database'''
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    '''Create the database schema if it doesn't exist'''
    Base.metadata.create_all(engine)

    '''Create a session to interact with the database'''
    Session = sessionmaker(bind=engine)
    session = Session()

    '''
    Add a new City "San Francisco" with a State "California"
    and establish the relationship
    '''
    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()
