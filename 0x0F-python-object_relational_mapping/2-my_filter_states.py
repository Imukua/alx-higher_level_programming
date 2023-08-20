#!/usr/bin/python3
"""
Script that connects  connects to a Mysql db and queries
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(user=sys.argv[2],
                         password=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         host='localhost')
    cur = db.cursor()
    query = '''SELECT *
               FROM `states
               WHERE BINARY `name` = "{}"'.format(sys.argv[4])
            '''
    cur = db.execute(query)
    stateList = cur.fetchall()
    for state in stateList:
        print(state)

    cur.close()
    db.clode()
