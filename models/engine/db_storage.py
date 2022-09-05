#!/usr/bin/python3
""" New engine DBStorage """

import os
from sqlalchemy.orm import Session, scoped_session, relationship
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """ private class attribute """
    __engine = None
    __session = None

    def __init__(self):
        """ metodo constructor init"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB"),
            pool_pre_ping=True))
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objs = []
        dic = {}
        print(cls)
        if cls is not None:
            objs = self.__session.query(cls)
            for obj in objs:
                key = ("{}.{}".format(type(cls).__name__, obj.id))
                dic[key] = obj
        else:
            for _str in ['State', 'City', 'Place', 'User', 'Review']:
                resul = self.__session.query(eval(_str)).all()
                print(resul)
                print(_str)
                for obj in resul:
                    key = _str + "." + obj.id
                    dic[key] = obj
                    print(dic)
        return dic

    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if obj is not None:
            self.__session.delete()

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ method on the private session attribute """
        self.__session.close()
