#!/usr/bin/python3
"""
Script that connects  connects to a Mysql db and queries
"""

import sys
import MySQLdb


if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(user=sys.argv[2],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         host='localhost')
    query = 'SELECT * FROM states WHERE name LIKE (N%) ORDER BY states.id'
    cur = db.cursor()
    cur.execute(query)
    stateList = cur.fetchall()
    for state in stateList:
        print(state)

    cur.close()
