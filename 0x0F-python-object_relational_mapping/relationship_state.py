#!/usr/bin/python3
"""
Defines a State model.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City

'''Create a base class for declarative models'''
Base = declarative_base()


class State(Base):
    """Represents a state for a MySQL database.
    """
    '''Specify the table name in the database'''
    __tablename__ = "states"

    '''Define columns and their data types'''
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    '''Define the relationship to the City model'''
    cities = relationship("City", backref="state", cascade="all, delete")
