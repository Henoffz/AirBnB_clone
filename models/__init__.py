#!/usr/bin/python3
"""
This module instantiate the file storage system.
"""
from models.engine.file_storage.py import FileStorage


cl_names = ["BaseModel", "User", "State", "City", "Place", "Amenity", "Review"]
cl_objects = [BaseModel, User, State, City, Place, Amenity, Review]

allclasses = dict(zip(cl_names, cl_objects))


storage = FileStorage()
storage.reload()
