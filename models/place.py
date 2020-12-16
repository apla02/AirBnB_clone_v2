#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from models.review import Review
from sqlalchemy.orm import relationship
from os import getenv
HBNB_STORAGE = getenv('HBNB_TYPE_STORAGE')

metadata = Base.metadata
place_amenity = Table('place_amenity', metadata, Column(
    'place_id', String(60), ForeignKey('places.id'), nullable=False),
    Column('amenity_id', String(60), ForeignKey(
        'amenities.id'), nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, default=0)
        number_bathrooms = Column(Integer, default=0)
        max_guest = Column(Integer, default=0)
        price_by_night = Column(Integer, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref='places', cascade='delete')
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False)
        amenity_ids = []

    else:
        place_amenity = Table
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            '''
            getter atributte to return the list of reviews
            '''
            reviews_dict = {}
            dictionary = models.storage.all(Review)
            for key, value in dictionary.items():
                    if self.id == Review.place_id:
                        reviews_dict[key] = value
            return reviews_dict.values()

        @property
        def amenities(self):
            """getter attribute amenities that returns the list of Amenity instances based
            """
            amenities_dict = {}
            dictionary = models.storage.all(Amenity)
            for key, value in dictionary.items():
                    if self.id == Place.place_id:
                        amenities_dict[key] = value
            return reviews_dict.values()

        @amenities.setter
        def amenities(self, value):
            """setter attribute amenities that handles append method
            """
            if isinstance(value, Amenity):
                    self.amenity_ids.append(value.id)
