#!/usr/bin/python3
"""
Get script that prints the first State object from
the database hbtn_0e_6_usa
"""

from sys import argv
from unicodedata import name

from sqlalchemy import (create_engine)

from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    tates = State(name="Louisiana")
    session.add(state)
    session.commit()
    row = session.query(State.id , State.name).filter(State.name == "Louisiana").first()
    if row is None:
        print("Not found")
    else:
        print(f"{row.id}")
