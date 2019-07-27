#!/usr/bin/python3

import sqlite3

connection_obj = sqlite3.connect("test.db")

try:
	cursor_object = connection_obj.cursor()
	print("created conn object successfully")
	cursor_object.execute("select * from student")
	
except:
	print("error in closing operation")

connection_obj.close()

