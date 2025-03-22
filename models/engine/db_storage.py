#!/usr/bin/python3
"""This DBStorage engine uses MySQL and SQLAlchemy"""
from models.base_model import BaseModel, Base
from models.user import User
from models.medication import Medication
from models.order import Order
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
import os

classes = {
    "BaseModel": BaseModel,
    "User": User,
    "Medication": Medication,
    "Order": Order
}

class DBStorage:
    """DBStorage class to manage PillPocket models in MySQL database"""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage engine"""
        user = os.getenv("PILLPOCKET_MYSQL_USER")
        passwd = os.getenv("PILLPOCKET_MYSQL_PWD")
        host = os.getenv("PILLPOCKET_MYSQL_HOST")
        db = os.getenv("PILLPOCKET_MYSQL_DB")
        env = os.getenv("PILLPOCKET_ENV")
        self.__engine = create_engine(f"mysql+mysqldb://{user}:{passwd}@{host}/{db}", pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)
        self.reload()
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)()

    def all(self, cls=None):
        """Query the database for all objects of a specific class"""
        if not self.__session:
            raise Exception("Session is not initialized")

        if cls:
            return {f"{cls.__name__}.{obj.id}": obj for obj in self.__session.query(cls).all()}
        else:
            objects = {}
            for model in classes.values():
                if model != BaseModel:
                    for obj in self.__session.query(model).all():
                        objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
            return objects

    def new(self, obj):
        """Add an object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session if it exists"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all database tables and initialize the session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Close the current database session"""
        self.__session.remove()
