#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database,
        port=3306,
        host='localhost'
    )

    cur = db.cursor()
    query = 'SELECT * FROM states ORDER BY id ASC'
    cur.execute(query)

    statesList = cur.fetchall()
    for state in statesList:
        print(state)

    cur.close()
    db.close()
