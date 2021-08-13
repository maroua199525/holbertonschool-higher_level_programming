#!/usr/bin/python3
"""Module state"""
import sys
import MySQLdb


def my_function():
    """Open database connection"""
    db = MySQLdb.connect("localhost", port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    """prepare a cursor object using cursor() method"""
    cursor = db.cursor()
    """execute SQL query using execute() method."""
    cursor.execute("SELECT * from states ORDER BY id ASC")
    result = cursor.fetchall()
    for state in result:
        print(state)
    cursor.close()
    db.close()

if __name__ == "__main__":
    my_function()