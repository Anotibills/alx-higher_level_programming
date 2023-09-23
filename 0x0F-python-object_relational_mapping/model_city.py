#!/usr/bin/python3
"""
Defines a City model.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

'''Create a base class for declarative models'''
Base = declarative_base()


class City(Base):
    """
    Represents a city for a MySQL database.
    """
    '''Specify the table name in the database'''
    __tablename__ = "cities"

    '''Define columns and their data types'''
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
