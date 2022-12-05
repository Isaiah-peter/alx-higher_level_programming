#!/usr/bin/python3
"""
create a model of city
"""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import State

Base = declarative_base()

class City(Base):
    """Create City"""
    __tablename__ = "cities"
    id = Column(Integer, nullable=False ,primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    states = relationship("States", back_populates="cities")

State = relationship("City", order_by=City.id,  back_populates="state")


