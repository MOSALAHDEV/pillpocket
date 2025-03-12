#!/usr/bin/python3
""" User class for representing user information in PillPocket"""
from models.base_model import BaseModel

class User(BaseModel):
    """ User class for representing user information in PillPocket"""
    def __init__(self, *args, **kwargs):
        """Initialize a new User instance."""
        super().__init__(*args, **kwargs)
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.password = ""