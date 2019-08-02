#!/usr/bin/python3

try: 
	fh =("records.txt","a")
	name = input("enter the student name")
	subject = input("enter the subject")
	rollno = input("enter your roll no")
	record ="{0},{1},{2}".format(name,rollno,subject)
	print(type(record))
	fh.write(record)
except Error as e:
	print(e)


