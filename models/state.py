#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import models
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states", cascade='delete')

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getter method to retrieve a list of cities
                where states_id is equal to current State.id
            """
            cities_dict = {}
            dictionary = models.storage.all(City)
            for key, value in dictionary.items():
                    if self.id == value.state_id:
                        cities_dict[key] = value
            return cities_dict.values()
