#!/usr/bin/python3
""" Order class for representing order information in PillPocket"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


class Order(BaseModel, Base):
    """ User class for representing user information in PillPocket"""
    __tablename__ = "orders"
    id = Column(String(60), primary_key=True)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    medication_id = Column(String(60), ForeignKey("medications.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    status = Column(String(50), default="Pending")

    # Relationship with User and Medication
    medication = relationship("Medication", back_populates="orders")
    user = relationship("User", back_populates="orders")

    def __init__(self, *args, **kwargs):
        """Initialize a new Order instance."""
        super().__init__(*args, **kwargs)
        if "status" not in kwargs:
            self.status = "Pending"
       # self.user_id = ""
       # self.medication_id = ""
       # self.quantity = 0
       # self.total_price = 0.0
       # self.order_date = ""
       # self.status = ""
