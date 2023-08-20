#!ussr/bin/python3

import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(username=sys.argv[1],
                         password=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states  WHERE name=%s ORDER BY id", (sys.argv[4], )
    cur = db.execute(query)
    stateList = cur.fetchall()
    for state in stateList:
        print(state)

    cur.close()
    db.close()
