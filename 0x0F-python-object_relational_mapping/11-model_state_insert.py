#!/usr/bin/python3
"""
Start linking class to table in database
and adds new object.
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    sesh = sessionmaker(bind=engine)
    session = sesh()

    data = State(name="Louisiana")
    session.add(data)
    session.commit()
    print(data.id)