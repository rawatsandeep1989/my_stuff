#!/usr/bin/python3

import sqlite3

try:
	connection_object = sqlite3.connect("test.db")
	cursor_object  = connection_object.cursor()
	print("cursor obj created")
	cursor_object.execute('''create table student(sid integer primary key,name varchar(20));''')
	print("Table created")

except:
	print("error")


#db.close()
