#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship

dbstorage = getenv('HBNB_TYPE_STORAGE')

class User(BaseModel, Base):
    __tablename__ = "users"
    """This is the class for user
    Attributes:
        email: email address String(128) can't be null
        password: password for you login String(128)
        first_name: first name String(128)
        last_name: last name String(128)
    """
    if dbstorage == 'database':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        
       # places = relationship("Place",  backref="user", cascade="all,delete")
       # reviews = relationship("Review",  backref="user", cascade="all,delete")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
