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
from os import getenv
from sqlalchemy.orm.session import make_transient
from sqlalchemy import inspect

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
        if our_env == 'test':
            Base.metadata.drop_all(self.__engine
                                   )
    def all(self, cls=None):
        """all objects depending of the class name (argument cls)"""
        cls_list = {}

        if cls:
            for line in self.__session.query(cls).all():
                val = line.__class__.__name__ + '.' + line.id
                cls_list[val] = line
        else:
            for l, c in self.__classes.items():
                for line in self.__session.query(c):
                    val = line.__class__.__name__ + '.' + line.id
                    cls_list[val] = line
        return cls_list

    def new(self, obj):
        """ Adds new obj to DB session """
        if inspect(obj).persistent:
            self.__session.expunge(obj)  # expunge the object from session
            make_transient(obj)  # make it transient
        self.__session.add(obj)

    def save(self):
        """ Commit changes to DB session """
        self.__session.commit()
    def delete(self, obj=None):
        """Delete from the current db"""
        if obj is not None:
            self.__session.delete(obj, synchronize_session=False)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """ Call delete method """
        self.__session.close()
 