#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models
import os

class State(BaseModel, Base):
    """ State class """


    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade = "all, delete")

    if os.getenv("HBNB_TYPE_STORAGE") != 'db':
        name = ""

        @property
        def cities(self):
            citylist = []
            city_dict = models.storage.all(City)
            for city in city_dict.values():
                if city.state_id == self.id:
                    citylist.append(city)
            return citylist
