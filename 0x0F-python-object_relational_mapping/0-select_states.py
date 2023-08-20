#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[2],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         host='localhost')

    cur = db.cursor()
    query = 'SELECT * FROM states'
    cur.execute(query)
    statesList = cur.fetchall()
    for state in statesList:
        print(state)

    cur.close()
    db.close()
