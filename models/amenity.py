#!/usr/bin/python3
'''
Represents amenity class  that inherits from BaseModel
'''
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Table
from sqlalchemy.orm import relationship
from models.place import place_amenity
from os import getenv
HBNB_STORAGE = getenv('HBNB_TYPE_STORAGE')


class Amenity (BaseModel, Base):
    '''
        Represents Class Amenity with public class attribute
    '''
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity)

    else:
        name = ''
