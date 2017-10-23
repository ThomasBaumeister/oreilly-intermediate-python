#!/usr/bin/python3

import sqlite3

connection=sqlite3.connect("jeopardy.db")

cursor=connection.cursor()

cursor.execute("select text,answer,value from clue limit 10")

results=cursor.fetchall()

for clue in results:
  text=clue[0]
  answer=clue[1]
  value=clue[2]

  print("[$%s]" % (value,))
  print("Question: %s" % (text,))
  print("Answer: What is '%s'?" % (answer,))
  print("")

connection.close()
