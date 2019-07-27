#!/usr/bin/python3


import MySQLdb
import json

with open("/home/sandeepr/mystuff/python_db_with_json_parsing/json_file.txt",'r') as f:
	data_in_json =json.load(f)


username=data_in_json['database']['username']
password=data_in_json['database']['passord']
db=data_in_json['database']['db']
hostname=data_in_json['database']['host']


# Open database connection
db = MySQLdb.connect(user=username,host=hostname,password=password,database=db )
print("mysql connection successfull")

#prepare a cursor object using cursor method
cursor = db.cursor()
print("cursor object obtained")

#execute a sql query using execute method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

# disconnect from server
db.close()
