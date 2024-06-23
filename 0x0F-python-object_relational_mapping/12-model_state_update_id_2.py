#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Changes the name of a State object from the database hbtn_0e_6_usa."""

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

    # Query the State object with id = 2
    state = session.query(State).filter_by(id=2).first()

    # Change the name of the State object
    if state:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()
