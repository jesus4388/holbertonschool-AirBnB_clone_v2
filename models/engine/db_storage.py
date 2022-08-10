#!/usr/bin/python3
'# New engine DBStorage'
import os
from sqlalchemy.orm import Session, scoped_session, relationship
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from models.user import User 
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    '#private class attribute'
    __engine = None
    __session = None


    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB"),
            pool_pre_ping=True))
        if os.getenv("HBNB_ENV") == "test":
            Base.metada.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        objs = []
        dic = {}
        if cls is None:
            str_clases = ['State', 'City']
            for str in str_clases:
                resul = self.__session.query(eval(str)).all()
                for obj in resul:
                    objs.append(obj)
        else:
            objs = self.__session.query(objs).all()
        for obj in objs:
            key = ("{}.{}".format(type(obj).__name__, obj.id))
            dic[key] = obj
        return dic
    
    def new(self, obj):
        """ add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session """
        if not obj is None:
            self.__session.delete()

    def reload(self):
        """ create all tables in the database """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
