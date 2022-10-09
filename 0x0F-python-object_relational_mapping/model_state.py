#!/usr/bin/python3
"""
sqlalchemy table
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """States"""
    __tablename__ = "states"
    id = Column(Integer,nullable=False ,primary_key=True)
    name = Column(String(128), nullable=False)