#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines a State class and an instance Base = declarative_base()."""

import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base
Base = declarative_base()


class State(Base):
    """State class that links to the MySQL table states."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    Base.metadata.create_all(engine)
