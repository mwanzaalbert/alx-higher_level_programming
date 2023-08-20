#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects,
contained in the database hbtn_0e_101_usa
Arguments:
    mysql_usr - username to connect the mySQL
    mysql psw - password to connect the mySQL
    db_name - Name of the database
"""


from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    mysql_usr = argv[1]
    mysql_pswd = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_usr, mysql_pswd, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    my_states = session.query(State).order_by(State.id)
    for state_instance in my_states:
        print("{}: {}".format(state_instance.id, state_instance.name))
        for city_instance in state_instance.cities:
            print("    {}: {}".format(city_instance.id, city_instance.name))
