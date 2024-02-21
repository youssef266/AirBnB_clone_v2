#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column("id", String(60), nullable=False, primary_key=True)
    created_at = Column("created_at", DATETIME, nullable=False,
                        default=datetime.utcnow())
    updated_at = Column("updated_at", DATETIME, nullable=False,
                        default=datetime.utcnow())
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
            for key, val in kwargs.items():
                if key != "__class__":
                    if ey in ["created_at", "updated_at"]:
                        setattr(self, key, datetime.fromisoformat(val))
                    else:
                        setattr(self, key, val)

    def __str__(self):
        """Returns a string representation of the instance"""
        clas = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(clas, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dic = dict(self.__dict__)
        dic['__class__'] = str(type(self).__name__)
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        try:
            del dic['_sa_instance_state']
        except KeyError:
            pass

        return dic

    def delete(self):
        """ delete object
        """
        from models import storage
        storage.delete(self)
