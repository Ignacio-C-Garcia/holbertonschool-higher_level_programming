#!/usr/bin/python3
""" a script that takes in the name of a state as an argument
and lists all cities of that state, using
the database hbtn_0e_4_usa"""
import MySQLdb
from sys import argv


def connection(user, psswd, datab, state):
    """function mysqldb"""
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
    cursor.execute("SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s", (state,))
    m = cursor.fetchall()
    separator = ""
    for item in m:
        print(separator, end="")
        print(item[0], end="")
        separator = ", "
    print("")


if __name__ == "__main__":
    connection(argv[1], argv[2], argv[3], argv[4])
