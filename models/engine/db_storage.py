#!/usr/bin/python3
"""The new engine to handle the databases"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os
from models.base_model import BaseModel, Base
from models.city import City
from models.state import State
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """New engine DBStorage
    """
    __engine = None
    __session = None

    classes = {
            'State': State, 'City': City,
            'User': User, 'Place': Place,
            'Review': Review, 'Amenity': Amenity
            }

    def __init__(self):
        """ instantiation DBStorage"
        """
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db, pool_pre_ping=True))
        if env == "test":
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on the current DB session all objects of a cls
        """
        dict_copy = {}
        if cls in DBStorage.classes.values():
            for objects in self.__session.query(cls).all():
                dict_copy[
                    objects.__class__.__name__ + "." + objects.id] = objects
        else:
            for class_name in DBStorage.classes.values():
                for objects in self.__session.query(class_name):
                    dict_copy[
                        objects.__class__.__name__ + "." + objects.id
                        ] = objects
        return(dict_copy)

    def new(self, obj):
        """add the object to the current database session

        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
