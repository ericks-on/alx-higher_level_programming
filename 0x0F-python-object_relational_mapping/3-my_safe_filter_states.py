#!/usr/bin/python3
"""this module contains a safe filter for database
when obtaining data from the states table
"""


import MySQLdb as sql
import  sys


def safe_filter(*args, **kargs):
    """this function filters states according to given name pattern
    and ensures no sql injections

    Args:
        user: username of mysql user
        password: password of the mysql user
        db: name of the database
        name: the pattern to match
    """
    try:
        db = sql.connect(user=sys.argv[1], passwd=sys.argv[2],
                         host='localhost', port=3306, db=sys.argv[3])
    except sql.Error as e:
        raise (e)
    else:
        c = db.cursor()
        name_query = "SELECT name FROM states"
        c.execute(name_query)
        names_result = c.fetchall()
        accepted_names = [item for tpl in names_result for item in tpl]
        name = sys.argv[4]
        if name in accepted_names:
            filter_query = """SELECT * FROM states WHERE name='{}'
            ORDER BY id""".format(name)
            c.execute(filter_query)
            result = c.fetchall()
            for row in result:
                print(row)
        else:
            print("Name does not exist!")
        c.close()
        db.close()


if __name__ == '__main__':
    safe_filter()
