#!/usr/bin/python3
"""uses MySQLdb to list cities in a database
"""

import sys
import MySQLdb as sql


def get_cities(*args, **kargs):
    """lists all cities from a database

    Args:
        username: username of the mysql server
        password: password of the user
        database: the database to obtain the cities

    """
    try:
        db = sql.connect(user=sys.argv[1], password=sys.argv[2],
                         host='localhost', port=3306, db=sys.argv[3])
    except sql.Error as e:
        raise (e)
    else:
        query = """SELECT cities.id, cities.name, states.name FROM cities
        INNER JOIN states ON states.id = cities.state_id ORDER BY id"""
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        for row in result:
            print(row)
        c.close()
        db.close()


if __name__ == '__main__':
    get_cities()
