#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id
            """
            from models.city import City
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]

