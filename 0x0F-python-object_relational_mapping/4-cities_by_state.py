#!/usr/bin/python3
"""a script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection(argv[1], argv[2], argv[3])


def connection(user, psswd, datab):
    try:
        db_connection = MySQLdb.connect(host="localhost",
                                        port=3306,
                                        user=user,
                                        passwd=psswd,
                                        db=datab,
                                        charset="utf8")
    except Exception as fail:
        raise fail
        return
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM cities\
            JOIN states ON cities.state_id = states.id")
    m = cursor.fetchone()
    while(m):
        print((m[0], m[2], m[4]))
        m = cursor.fetchone()
