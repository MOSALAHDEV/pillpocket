#!/usr/bin/python3
""" User class for representing drug information in PillPocket"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.orm import relationship


class Medication(BaseModel, Base):
    """ Medication class for representing user information in PillPocket"""
    __tablename__ = "medications"
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False, unique=True)
    price = Column(Float, nullable=False)
    dosage = Column(String(128), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    # Relationship with Order
    orders = relationship("Order", back_populates="medication")

    def __init__(self, *args, **kwargs):
        """Initialize a new Medication instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
        self.manufacturer = ""
        self.price = 0.0
        self.expiry_date = ""
        self.stock = 0
