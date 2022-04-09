#!/usr/bin/python3
"""a script that lists all states with a name starting with N from
the database hbtn_0e_0_usa"""
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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    m = cursor.fetchone()
    if (m == None):
        print("")
    while(m):
        print(m)
        m = cursor.fetchone()
