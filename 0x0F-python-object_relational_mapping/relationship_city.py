#!/usr/bin/python3
'''
module 'model_city'
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base, State

class City(Base):
    '''
    Class definition of a city.
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    '''
    Define a relationship to the State model
    '''
    state = relationship("State", back_populates="cities")
    state_id = Column(Integer, ForeignKey('states.id'))
