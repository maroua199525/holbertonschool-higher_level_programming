#!/usr/bin/python3
"""
 script that takes in arguments and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument.
 But this time, write one that is safe from MySQL injections!

"""
import sys
import MySQLdb


def main(argv):
    """a script should connect to a MySQL """
    connect = MySQLdb.connect(host="localhost", port=3306,
                              user=argv[1], passwd=argv[2], db=argv[3])
    cursor = connect.cursor()
    arg = MySQLdb.escape_string(argv[4]).decode()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}%'\
                ORDER BY id ASC".format(arg))
    current = cursor.fetchall()
    for row in current:
        print(row)
    pass
    cursor.close()
    connect.close()


if __name__ == '__main__':
    if len(sys.argv) == 5:
        main(sys.argv)
