#!/usr/bin/python3
"""
 This file declares a class that manage database storage """
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """"""
    __engine = None
    __session = None
    __classes = {
                'BaseModel': BaseModel, 'User': User, 'Place': Place,
                'State': State, 'City': City, 'Amenity': Amenity,
                'Review': Review
                }

    def __init__(self):
        """ Class that creates elements of our MySql """
        our_user = getenv('HBNB_MYSQL_USER')
        our_pwd = getenv('HBNB_MYSQL_PWD')
        our_host = getenv('HBNB_MYSQL_HOST')
        our_db = getenv('HBNB_MYSQL_DB')
        our_env = getenv('HBNB_ENV')

	self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(our_user, our_pwd, our_host, our_db),pool_pre_ping=True)

    def new(self, obj):
        """ Adds new obj to DB session """
        self.__session.merge(obj)

    def save(self):
        """ Commit changes to DB session """
        self.__session.commit()
