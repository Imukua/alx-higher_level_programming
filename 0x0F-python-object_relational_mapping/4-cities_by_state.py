#!ussr/bin/python3


if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(username=sys.argv[1],
                         password=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()

    cur = db.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id"""
    )
    cityList = cur.fetchall()
    for city in cityList:
        print(city)

    cur.close()
    db.close()
