#!/usr/bin/python3
"""Defines the city class.""" 
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

from os import getenv

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        name = ''
        state_id = ''