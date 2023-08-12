#!/usr/bin/python3
"""
This module contain a class 'User' that
inherits from BaseModel class.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    The User class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
