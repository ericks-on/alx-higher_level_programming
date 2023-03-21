#!/usr/bin/python3
"""script that takes name of state as an argument
and lists all cities of that state

Args:
    user: user of mysql server
    password: password of the user
    database: name of the database
    state_name: name of the state to get the cities
"""

import sys
import MySQLdb as sql


def state_cities(state_name):
    """this function gets a state as an argument and lists the cities

    Args:
        state_name: the name of the state to get the cities

    """
    try:
        db = sql.connect(user=sys.argv[1], password=sys.argv[2],
                         db=sys.argv[3], host='localhost', port=3306)
    except sql.Error as e:
        raise (e)
    else:
        c = db.cursor()
        query = """SELECT states.name, cities.name FROM
        states INNER JOIN cities ON states.id = cities.state_id ORDER BY
        cities.id"""
        c.execute(query)
        tuple_combo = c.fetchall()
        states = [item[0] for item in tuple_combo]
        if state_name in states:
            cities = [item[1] for item in tuple_combo if item[0] == state_name]
            i = 0
            while i < len(cities):
                if i == (len(cities) - 1):
                    print(cities[i])
                    break
                print(cities[i], end=", ")
                i += 1
        else:
            print()


if __name__ == "__main__":
    state_cities(sys.argv[4])
