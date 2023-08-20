#!/usr/bin/python3
"""
Script that connects  connects to a Mysql db and queries all stats
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost'
    )

    query = '''
        SELECT * \
        FROM states \
        WHERE name LIKE BINARY "N%" \
        ORDER BY states.id ASC
    '''
    cur = db.cursor()
    cur.execute(query)
    stateList = cur.fetchall()
    for state in stateList:
        print(state)

    cur.close()
    db.clode()
