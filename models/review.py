#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Review(BaseModel):
    """This is the class for Review
    Attributes:
        place_id: place id String(1024)can't be null
        user_id: user id String(60) can't be null
        text: review description
    """
    #__tablename__ = "reviews"
    #text = Column(String(1024), nullable=False)
    #place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    #user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
