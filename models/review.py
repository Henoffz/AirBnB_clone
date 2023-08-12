#!/usr/bin/python3
"""
This module inherits from the BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The review class and its public attributes
    """
    place_id = ""
    user_id = ""
    text = ""
