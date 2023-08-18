#!/usr/bin/python3

import MySQLdb
import sys

db = hbtn_0e_0_usa.connect(username = sys.argv[2],
                           password = sys.argv[2],
                           db = sys.argv[3],
                           port = 3306,
                           host = 'localhost')

cur = db.cursor()
query = 'SELECT * FROM states'
cur.execute(query)
statesList = [row[0] for row in cur.fetchall]
for state in statesList:
    print(state)
