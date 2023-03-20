#!/usr/bin/python3
"""this module uses MySQLdb
"""

import MySQLdb as sql
import sys


def filter_states(*args, **argv):
    """obtains states that start with uppper N from the given database.
    The database is given as an argument to the script

    Args:
        user:the mysql user
        passwd: the user password
        db: the database to obtain the states
    """
    try:
        db = sql.connect(host='localhost', port=3306, user=sys.argv[1],
                        passwd=sys.argv[2], db=sys.argv[3])
    except sql.Error as e:
        raise (e)
    else:
        c = db.cursor()
        c.execute("""SELECT * from states WHERE name LIKE
                'N%' ORDER BY id""")
        result = c.fetchall()
        if result:
            for row in result:
                print(row)
        c.close()
        db.close()


if __name__ == "__main__":
    filter_states()
