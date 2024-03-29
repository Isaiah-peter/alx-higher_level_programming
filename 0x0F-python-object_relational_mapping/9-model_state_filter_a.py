#!/usr/bin/python3
"""
find state that have a
"""

from sys import argv

from model_state import State
from sqlalchemy.orm import sessionmaker


from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    rows = session.query(State.id, State.name).filter(State.name.like('%a%')).order_by(State.id)

    for row in rows:
        print(f"{row.id}: {row.name}")