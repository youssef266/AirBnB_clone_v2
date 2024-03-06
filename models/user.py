#!/usr/bin/python3


"""This is the user class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review

dbstorage = getenv('HBNB_TYPE_STORAGE')

class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address String(128) can't be null
        password: password for you login String(128)
        first_name: first name String(128)
        last_name: last name String(128)
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    if dbstorage == 'db':
        places = relationship("Place", cascade="all, delete", backref="user")
        reviews = relationship("Review", cascade="all, delete", backref="user")
    else:
        @property
        def places(self):
            """Getter attribute that returns the list of Place instances
            where the user_id is equal to the current User.id"""
            from models import storage
            places_list = []
            for place in storage.all(Place).values():
                if place.user_id == self.id:
                    places_list.append(place)
            return places_list

        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances
            where the user_id is equal to the current User.id"""
            from models import storage
            reviews_list = []
            for review in storage.all(Review).values():
                if review.user_id == self.id:
                    reviews_list.append(review)
            return reviews_list
