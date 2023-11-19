#!/usr/bin/python3
"""Prints State object with the name passed
as an argument from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Create connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Creating configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create Session
    session = Session()

    state_name = sys.argv[4]
    result = session.query(State).filter(State.name == state_name).first()

    if result:
        print(result.id)
    else:
        print("Not found")
