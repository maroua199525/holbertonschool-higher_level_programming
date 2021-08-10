#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


def my_function():
    """Open database connection"""
    db = MySQLdb.connect("localhost", port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    """prepare a cursor object using cursor() method"""
    cursor = db.cursor()
    """execute SQL query using execute() method."""
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id")
    result = cursor.fetchall()
    for state in result:
        if state[1][0] =='N':
            print(state)
    db.close()

if __name__ == "__main__":
    my_function()
