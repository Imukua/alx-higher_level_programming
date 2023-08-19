#!ussr/bin/python3

import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(username=sys.argv[1],
                         password=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    query = 'SELECT * FROM `states` WHERE name LIKE (N%) ORDER BY `id`'
    cur = db.cursor()
    cur.execute(query)
    stateList = [row[0] for row in cur.fetchall()]
    for state in stateList:
        print(state)
