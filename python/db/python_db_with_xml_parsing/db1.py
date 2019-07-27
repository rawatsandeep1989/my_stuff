#!/usr/bin/python3


import xml.dom.minidom

#note : change location of file here:
DOMtree = xml.dom.minidom.parse("/home/sandeepr/python_learn/config.xml")

collection = DOMtree.documentElement

if collection.hasAttribute("title"):
	print("Root element  %s" % collection.getAttribute("title"))

dbs = collection.getElementsByTagName("database")

for db in dbs:
	print("db name:")
	if db.hasAttribute("title"):
		print("Title %s" % db.getAttribute("title"))

	hostname = db.getElementsByTagName("hostname")[0]
	print("hostname %s" % hostname.childNodes[0].data)

	username = db.getElementsByTagName("username")[0]
	print("username : %s" % username.childNodes[0].data)


