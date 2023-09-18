#!/usr/bin/python3
"""Script that adds a new State object to the database 
hbtn_0e_6_usa and retrieves its ID"""

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    '''Check if the correct number of command-line arguments is provided'''
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    '''Get command-line arguments'''
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    '''Create a database connection'''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        username, password, database), pool_pre_ping=True)

    '''Create a session'''
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        '''
        Create a new State object with the name 'Louisiana'
        '''
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()
        '''
        Retrieve the State object with the name 'Louisiana'
        '''
        louisiana = session.query(State).filter_by(name='Louisiana').first()

        if louisiana:
            print(louisiana.id)
        else:
            print("Louisiana not found")

    except Exception as e:
        print("Error: {}".format(e))
        sys.exit(1)

    finally:
        # Close the session
        session.close()
