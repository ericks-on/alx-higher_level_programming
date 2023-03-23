#!/usr/bin/python3
"""script lists all states from the a database

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


def get_states():
    """this functions obtains states from a database

    """
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1],
                                                           sys.argv[2],
                                                           sys.argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).order_by(State.id)
    for r in result:
        print(f"{r.id}: {r.name}")


if __name__ == "__main__":
    get_states()
