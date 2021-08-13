#!/usr/bin/python3
"""
  a script that takes in the name of a state as an argument and
  lists all cities of that state,
  using the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id", (argv[4], ))
    list = []
    for cities in cursor.fetchall():
        for name in cities:
            list.append(name)
    print(", ".join(list))
    cursor.close()
    db.close()
