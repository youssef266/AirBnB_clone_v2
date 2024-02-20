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

    def all(self, cls=None):
        """all objects depending of the class name (argument cls)"""
        if clas is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(clas) == str:
                clas = eval(clas)
            objs = self.__session.query(clas)
        return {"{}.{}".format(type(obj).__name__, obj.id):
                obj for obj in objs}

    def new(self, obj):
        """ Adds new obj to DB session """
        self.__session.merge(obj)

    def save(self):
        """ Commit changes to DB session """
        self.__session.commit()
    def delete(self, obj=None):
        """Delete from the current db"""
        if obj is not None:
            self.__session.delete(obj)
