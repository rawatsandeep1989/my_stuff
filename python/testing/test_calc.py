#!/usr/bin/python3

import unittest

import calc


class TestClass(unittest.TestCase):
	def test_add(self):
		self.assertEqual(calc.add(1,2),154)
		self.assertEqual(calc.add(3,3),6)

if __name__ == '__main__':
	print(__name__)
	unittest.main()
