#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
storage_var = os.getenv('HBNB_TYPE_STORAGE')

if storage_var == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
