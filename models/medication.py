#!/usr/bin/python3
""" User class for representing drug information in PillPocket"""
from models.base_model import BaseModel

class Medication(BaseModel):
    """ Medication class for representing user information in PillPocket"""
    def __init__(self, *args, **kwargs):
        """Initialize a new Medication instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
        self.manufacturer = ""
        self.price = 0.0
        self.expiry_date = ""
        self.stock = 0