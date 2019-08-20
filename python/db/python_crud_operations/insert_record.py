#!/usr/bin/python3

import sqlite3

connection_object = sqlite3.connect("test.db")
name = input("enter the name")
sid = input("enter the sid ")
sql_query = "insert into student(sid,name) values({0},'{1}');".format(sid, name)
print(sql_query)

try:
	cursor_object = connection_object.cursor()
	cursor_object.execute(sql_query)
	connection_object.commit()
	print("inserted")
except ConnectionError as e:
	connection_object.rollback()

connection_object.close() 


