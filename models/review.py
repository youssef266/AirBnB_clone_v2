#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float


class Review(BaseModel, Base):
    """This is the class for Review
    Attributes:
        __tablename__: table name, reviews
        text: review description
        place_id: place id String(60) can't be null, foreign key to places.id
        user_id: user id String(60) can't be null, foreign key to users.id
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
