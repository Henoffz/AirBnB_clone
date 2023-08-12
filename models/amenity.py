#!/usr/bin/python3
"""
This module inherits from the
BaseModel
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    The Amenity class and it public attribute
    """
    name = ""
