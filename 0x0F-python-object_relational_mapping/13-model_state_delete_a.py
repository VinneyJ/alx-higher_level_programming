#!/usr/bin/python3
"""
Start linking class to table in database
delete names containing 'a'
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

    data = session.query(State).filter(State.name.contains("a"))
    for item in data:
        session.delete(item)
    session.commit()
