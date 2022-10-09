#!/usr/bin/python3
"""
sqlalchemy table
"""

from unicodedata import name
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class States(Base):
    __tablename__ = "states"
    id = Column(Integer,nullable=False ,primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return "<States name = %(name)s, >" % {self.name}