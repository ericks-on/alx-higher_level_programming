#!/usr/bin/python3
"""this module uses MySQLdb
"""

import MySQLdb as sql
import sys


def obtain_states(*args, **argv):
    db = sql.connect(host='localhost', port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT * from states WHERE name LIKE
            'N%' ORDER BY id""")
    for row in c.fetchall():
        print(row)
    c.close()
    db.close()


if __name__ == "__main__":
    obtain_states()
