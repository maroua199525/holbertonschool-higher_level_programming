#!/usr/bin/python3
""" a script that prints the State object with the name passed
    as argument from the database hbtn_0e_6_usa."""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    cursor = session.query(State).filter(State.name == argv[4]).first()
    if not cursor:
        print("Not found")
        exit
    else:
        print(cursor.id)
