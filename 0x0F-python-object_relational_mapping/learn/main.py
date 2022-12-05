#!/usr/bin/python3


from datetime import datetime
import sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base  = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    date_created = Column(DateTime(), nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.id}, {self.username}, {self.email}, {self.date_created} >"


user = User(id=1, username="Peter Isaiah", email="peterisaiah4fun@gmail.com", date_created=datetime.now())

print(user)