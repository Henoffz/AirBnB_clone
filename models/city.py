#!/usr/bin/python3
"""
This module inherits from
the BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    The City class and its public attributes
    """
    state_id = ""
    name = ""
