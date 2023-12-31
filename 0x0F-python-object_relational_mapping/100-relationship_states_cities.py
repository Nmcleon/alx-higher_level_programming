#!/usr/bin/python3
"""Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    # Create connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Create State and City objects
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)

    # Add State and City to the session and commit changes
    session.add(new_state)
    session.add(new_city)
    session.commit()
