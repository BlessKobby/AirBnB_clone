#!/usr/bin/python3
"""Module to create User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class repository for users objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
