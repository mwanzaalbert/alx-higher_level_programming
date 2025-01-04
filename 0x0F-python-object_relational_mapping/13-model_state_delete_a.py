#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Deletes all State objects with a name containing the letter 'a'.

from the database hbtn_0e_6_usa.
"""

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

    try:
        # Perform a bulk delete for all State objects with 'a' in their name
        session.query(State).filter(State.name.ilike('%a%')
                                    ).delete(synchronize_session='fetch')

        # Commit the transaction
        session.commit()
    except Exception as e:
        # Rollback the transaction in case of an error
        session.rollback()
        print(f"Error occurred: {e}")
    finally:
        # Close the session
        session.close()
