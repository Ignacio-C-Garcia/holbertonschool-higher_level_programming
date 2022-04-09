#!/usr/bin/python3
import MySQLdb
from sys import argv

db_connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
cursor = db_connection.cursor()
cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", (argv[4],))
m = cursor.fetchone()
while(m):
    print(m)
    m = cursor.fetchone()
