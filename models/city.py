#!/usr/bin/python3
"""Defines the city class.""" 
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Foreignkey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = column(String(60), Foreignkey("states.id"), nullable=False)
        places = relationship("Place", backref = "cities", cascade = "delete")
