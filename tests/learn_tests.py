"""
Testing suite to incorporate along with all of the testing exercises I am working on.
"""


from nose.tools import *


from learn import learnre


def setup():
	print "SETUP!"

def teardown():
	print "TEAR DOWN!"

def test_basic():
	print "I RAN!"

def test_learnre():
	mctesty = learnre.RE("tests/tester.txt")
	

if __name__ == "__main__":
	test_basic()