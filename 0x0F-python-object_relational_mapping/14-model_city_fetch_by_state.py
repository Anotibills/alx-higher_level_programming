#!/usr/bin/python3
"""Script that lists all City objects from the database hbtn_0e_14_usa with their associated State names"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    '''Check if the correct number of command-line arguments is provided'''
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    '''Create a database connection'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    '''Create a session'''
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        '''Query City objects with their associated State names'''
        city_state_pairs = session.query(City, State).filter(City.state_id == State.id).all()

        for city, state in city_state_pairs:
            print('{}: ({}) {}'.format(state.name, city.id, city.name))

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

    finally:
        # Close the session
        session.close()
