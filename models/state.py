#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
import os
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "fs":
        @property
        def cities(self):
            citylist = []
            city_dict = models.storage.all(models.city.City)
            for key, value in city_dict.items():
                if value.state_id == self.id:
                    citylist.append(value)
            return citylist

    if os.getenv("HBNB_TYPE_STORAGE") == "fs": 
    	cities = relationship("City", cascade = "all,delete", backref="state")
