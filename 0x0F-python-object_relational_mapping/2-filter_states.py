"""this module contains function to filter states in adatabase 
"""

import sys 
import MySQLdb as sql


def filter_states(*args, **argv):
    """this function filters states according to given name pattern

    Args:
        user: username of mysql user
        password: password of the mysql user
        db: name of the database
        name: the pattern to match
    """
    try:
        db = sql.connect(user=sys.argv[1], password=sys.argv[2], db=sys.argv[3]
                         host='localhost', port=3306)
    except sql.Error as e:
        raise (e)
    else:
        pattern = sys.argv[4]
        table = 'states'
        my_query = "SELECT * FROM {} WHERE name={} ORDER BY id".format(table,
                pattern)
        c = db.cursor()
        c.execute(my_query)
        result = c.fetchall()
        if result:
            for row in result:
                print (row)
        c.close()
        db.close()


if __name__ == "__main__":
    filter_states()
