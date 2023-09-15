#!/usr/bin/python3
'''
module 'model_city'
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

class City(Base):
    '''
    Class definition of a city.
    '''

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    
    # Define a relationship to the State model
    state = relationship("State", back_populates="cities")
