#!/usr/bin/python3
"""this module uses MySQLdb
"""

import MySQLdb as sql
import sys


def obtain_states(*args, **argv):
    """obtains states from the given database.
    The database is given as an argument to the script

    Args:
        user:the mysql user
        passwd: the user password
        db: the database to obtain the states
    """

    db = sql.connect(host='localhost', port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * from states ORDER BY id""")
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()


if __name__ == "__main__":
    obtain_states()
