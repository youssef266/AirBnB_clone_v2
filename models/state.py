#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column("name", String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """ Getter method
            Returns listof instances """
            from models import storage

            clist = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    clist.append(value)

            return clist
