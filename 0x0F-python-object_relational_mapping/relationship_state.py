#!/usr/bin/python3
'''
module 'base_model'
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class State(Base):
    '''
    Class definition of a state.
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    '''
    Define a one-to-many relationship with City
    '''
    cities = relationship("City", backref="state")
