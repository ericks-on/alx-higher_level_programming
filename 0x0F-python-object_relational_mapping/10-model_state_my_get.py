#!/usr/bin/python3
"""this script prints the state object with the name passed as an argument
"""

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
from model_state import State, Base


def search_state(user, passwd, db, state):
    """This function searches for the state passed as an argument and prints
    it if it exists in the database

    Args:
        user: user of mysql server
        passwd: password of the user
        db: database to obtain the states
        state: the name of the state to search

    """
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, passwd, db)

    # creating the engine to connect to mysql
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # obtaining list of valid search names
    valid_names = [row.name for row in session.query(State).all()]

    # making the filtered query
    if state in valid_names:
        result = session.query(State).filter_by(name=state).first()
        print(result.id)
    else:
        print('Not found')


if __name__ == '__main__':
    search_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
