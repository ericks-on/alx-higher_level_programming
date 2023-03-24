#!/usr/bin/python3
"""script that prints the first state from the a database

Args:
    username: username of the mysql user
    password: the password of the user
    database: database to obtain the states

"""

import sqlalchemy
from model_state import State, Base
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def first_state():
    """this function prints first state from the database
    """
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1],
                                                           sys.argv[2],
                                                           sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).first()
    if first:
        print(f"{first.id}: {first.name}")
    else:
        print()


if __name__ == "__main__":
    first_state()
