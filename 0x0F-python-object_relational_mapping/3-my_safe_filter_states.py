#!/usr/bin/python3
"""a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!"""
import MySQLdb
from sys import argv

db_connection = MySQLdb.connect(host="localhost",
                                port=3306,
                                user=argv[1],
                                passwd=argv[2],
                                db=argv[3],
                                charset="utf8")
cursor = db_connection.cursor()
cursor.execute("SELECT * FROM states\
        WHERE name LIKE %s ORDER BY id ASC", (argv[4],))
m = cursor.fetchone()
while(m):
    print(m)
    m = cursor.fetchone()
