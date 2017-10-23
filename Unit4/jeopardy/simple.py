#!/usr/bin/python3

import sqlite3

connection=sqlite3.connect("jepordy.db")

cursor=connection.cursor()

cursor.execute("select name from category limit 10")

for category in cursor.fetchall():
	print (category[0])

connection.close()
