#!/usr/bin/python3
"""this script lists all objects that start with a letter a
ffrom the database
"""

import sqlalchemy
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base


def a_states(user, passwd, db):
    """This functions list all the states that contain letter a

    Args:
        user: this is the user of the server
        passwd: password of the user
        db: the database to obtain the states

    """
    url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, passwd, db)

    # creating engine and session

    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # querying
    result = session.query(State).filter(State.name.like('%a%')).all()
    if result:
        for r in result:
            print(f'{r.id}: {r.name}')
    else:
        print()


if __name__ == '__main__':
    a_states(sys.argv[1], sys.argv[2], sys.argv[3])
