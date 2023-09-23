#!/usr/bin/python3
"""
Script that start link class to table in the database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    '''Create a SQLAlchemy engine for the specified database'''
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    '''
    Create the database tables based on the defined models (declarative_base)
    '''
    Base.metadata.create_all(engine)
