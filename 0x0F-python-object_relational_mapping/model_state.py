#!/usr/bin/python3
'''
Module 'base_model'
'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a declarative base
Base = declarative_base()


class State(Base):
    '''
    Class definition of a state.
    '''

    __tablename__ = 'states'

    # Define columns
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
