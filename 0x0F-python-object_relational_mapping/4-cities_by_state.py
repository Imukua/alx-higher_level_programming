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
    query = 'SELECT `c`.`id`, `c`.`name`,`s`.`name` \
                FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                    ON `c`.`id` = `s`.`id` \
                ORDER BY `c`.`id`'
                    

    cur = db.execute(query)
    cityList = [row[0] for row in cur.fetchall()]
    for city in cityList:
        print(city)