"""
Testing suite to incorporate along with all of the testing exercises I am working on.
"""


from nose.tools import *
import unittest

from learn import learnre
from learn import magicmethods


def setup():
	print "SETUP!"

def teardown():
	print "TEAR DOWN!"

def test_basic():
	print "I RAN!"

class TestRE(unittest.TestCase):

	def test_learnre(self):
		mctesty = learnre.RE("tests/tester.txt")
	
class TestMagicMethods_Word(unittest.TestCase):

	def setUp(self):
		self.word1 = magicmethods.Word("Example")
		self.word2 = magicmethods.Word("Example ")
		self.word3 = magicmethods.Word("Examples")


	def test_the_world_is_sane(self):
		self.assertEquals(1+1, 2)

	def test_word_class_methods(self):
		
		#remove whitespace
		self.assertEquals(self.word1, self.word2)
		self.assertLessEqual(self.word1, self.word2)
		
		# Not equal length
		self.assertLess(self.word1, self.word3)

		# Greater than
		self.assertGreater(self.word3, self.word1)

		# Lesser then

	def test_word_type(self):
		self.assertEquals(type(self.word1), type(self.word2))

class TestMagicMethods(unittest.TestCase):

	def setUp(self):
		pass

if __name__ == "__main__":
	test_basic()