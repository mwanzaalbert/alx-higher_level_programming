#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Lists all State objects from the database hbtn_0e_6_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create an engine that connects to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Bind the engine to the Base's metadata
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Query all State objects and order by states.id
    states = session.query(State).order_by(State.id).all()

    # Print the results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
