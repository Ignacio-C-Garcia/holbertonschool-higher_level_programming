#!/usr/bin/python3
"""a script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa where
name matches the argument"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_connection = MySQLdb.connect(host="localhost",
                                    port=3306,
                                    user=argv[1],
                                    passwd=argv[2],
                                    db=argv[3],
                                    charset="utf8")
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states\
            WHERE name = '{}' ORDER BY id ASC".format(argv[4]))
    m = cursor.fetchone()
    while(m):
        print(m)
        m = cursor.fetchone()
