#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from models.review import Review
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata, Column(
    'place_id', String(60), ForeignKey(
        'places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey(
        'amenities.id'), primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
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

    if getenv('HBNB_TYPE_STORAGE') != 'db':
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
            from models.amenity import Amenity
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
            from models.amenity import Amenity
            if isinstance(value, Amenity):
                    self.amenity_ids.append(value.id)
