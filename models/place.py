#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models import storage
import os
from models.review import Review
from models.amenity import Amenity  

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    # For DBStorage
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", cascade="all, delete", backref="place")

    # For FileStorage
    if os.getenv("HBNB_TYPE_STORAGE") == "file":
        @property
        def reviews(self):
            """Getter attribute that returns the list of Review instances
            with place_id equals to the current Place.id"""
            review_list = []
            for review in storage.all("Review").values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list
# For DBStorage
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)

    # For FileStorage
    if os.getenv("HBNB_TYPE_STORAGE") == "file":
        @property
        def amenities(self):
            """Getter attribute that returns the list of Amenity instances
            based on the attribute amenity_ids that contains all Amenity.id linked to the Place"""
            amenity_list = []
            for amenity_id in self.amenity_ids:
                amenity = storage.get("Amenity", amenity_id)
                if amenity is not None:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, amenity):
            """Setter attribute that handles append method for adding an Amenity.id
            to the attribute amenity_ids. This method should accept only Amenity object, otherwise, do nothing."""
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)