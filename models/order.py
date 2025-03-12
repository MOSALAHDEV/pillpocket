#!/usr/bin/python3
""" Order class for representing order information in PillPocket"""
from models.base_model import BaseModel


class Order(BaseModel):
    """ User class for representing user information in PillPocket"""
    def __init__(self, *args, **kwargs):
        """Initialize a new Order instance."""
        super().__init__(*args, **kwargs)
        self.user_id = ""
        self.medication_id = ""
        self.quantity = 0
        self.total_price = 0.0
        self.order_date = ""
        self.status = ""