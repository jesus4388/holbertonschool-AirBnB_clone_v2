#!/usr/bin/python3
'# New engine DBStorage'
import os
from sqlalchemy.orm import create_engine

class DBStorage:
    '#private class attribute'
    __engine = None
    __session = None


    __init__(self):
        self.engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv("HBNB_MYSQL_USER"),
            os.getenv("HBNB_MYSQL_PWD"),
            os.getenv("HBNB_MYSQL_HOST"),
            os.getenv("HBNB_MYSQL_DB"),
            pool_pre_ping=True))
        if os.getenv(HBNB_ENV) == test:
            Base.metada.drop_all(bind=self.__engine)
