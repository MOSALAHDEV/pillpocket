#!/usr/bin/python3
""" User class for representing user information in PillPocket"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ User class for representing user information in PillPocket"""
    __tablename__ = 'users'
    id = Column(String(60), primary_key=True)
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    orders = relationship("Order", back_populates="user")

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance."""
        super().__init__(*args, **kwargs)
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.password = ""
