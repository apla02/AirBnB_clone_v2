#!/usr/bin/python3
'''
Represents amenity class  that inherits from BaseModel
'''
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    '''
        Represents Class Amenity with public class attribute
    '''
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
