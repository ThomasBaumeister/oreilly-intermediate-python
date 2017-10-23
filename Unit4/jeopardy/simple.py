#!/usr/bin/python3

import sqlite3

connection=sqlite3.connect("jeopardy.db")

print (connection)

cursor=connection.cursor()

cursor.execute("select text from clue limit 10")

for category in cursor.fetchall():
	print (category[0])

connection.close()
