#!/usr/bin/python3
""" """
import models
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.state import State
from sqlalchemy.exc import OperationalError

class test_City(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_creation(self):
        """ """
        state = State(name="California")
        state.save()
        new = self.value(state_id=state.id, name="San_Francisco")
        self.assertEqual(type(new.state_id), str)
        self.assertEqual(type(new.name), str)
        new.save()
        """ models.storage._DBStorage__session.add(new)
        models.storage._DBStorage__session.commit()
        models.storage._DBStorage__session.rollback() """

    """ def test_no_arg(self):
        """ """
        new = self.value()
        with self.assertRaises(OperationalError):
            models.storage.__session.rollback()
            new.save() """
