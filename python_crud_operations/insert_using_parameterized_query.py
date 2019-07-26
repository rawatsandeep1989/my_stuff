#!/usr/bin/python3

import sqlite3

connection_obj = sqlite3.connect("test.db")
sql_query = "insert into student(sid,name) values(?,?);"

try:
	cursor_obj = connection_obj.cursor()
	print("creating a cursor object")
	cursor_obj.execute(sql_query,(11,'sam'))
	print("executing a parameterized query")
	connection_obj.commit()
	print("one record added successfully")
except:
	print("error in operation")
	connection_obj.rollback()

connection_obj.close()
	


