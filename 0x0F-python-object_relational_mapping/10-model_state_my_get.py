#!/usr/bin/python3
"""
Start linking class to table in database
return the id of the existing arg
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

    query = session.query(State).order_by(State.id)
    trigger = 0
    for line in query:
        if line.name == sys.argv[4]:
            print("{}".format(line.id))
            trigger += 1
    if trigger == 0:
        print("Not found")
