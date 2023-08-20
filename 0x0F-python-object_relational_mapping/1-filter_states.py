#!/usr/bin/python3
"""
Script that connects  connects to a Mysql db and queries all stats
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        user=username,
        password=password,
        db=database,
        port=3306,
        host='localhost'
    )
    
    query = '''
        SELECT * 
        FROM states 
        WHERE name LIKE "N%" 
        ORDER BY id ASC
    '''
    cur = db.cursor()
    cur.execute(query)
    stateList = cur.fetchall()
    for state in stateList:
        print(state)

    cur.close()
    db.clode()
