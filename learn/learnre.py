
"""
Exercises for working with Python Regex. While not perfect, at least it is a start.

Lots of violation of DRY principle here, but didn't realize the exercises would be so repetetive. 

Nathan Danielsen
nathan.danielsen@gmail.com

Source Docs:
http://www.ucs.cam.ac.uk/docs/course-notes/unix-courses/PythonRE/files/PythonRE.pdf
"""

### Imports
import sys
import re

### Main

class RE(object):
	def __init__(self, file):
		self.file = open(file, "r")
	
	def initprint(self):
		print "The file is open!"
		#print "PROOF ==> The first line is: '%s'" % (self.file.readline())
	
	
	def research(self, pattern):
		"""
		For single or simple regular expressions
		"""

		regexp = re.compile(pattern)
		for line in self.file:
			result = regexp.search(line)
			if result:
				print line

	def group_research(self, pattern):
		"""
		For grouping of single or simple regular expressions
		"""

		regexp = re.compile(pattern)
		for line in self.file:
			result = regexp.search(line)
			if result:
				print result.group(1), result.group(2)

	def verb_research(self, pattern):
		"""
		For multiple line or complex regular expressions

		"""
		regexp = re.compile(pattern, re.I+re.VERBOSE)
		for line in self.file:
			result = regexp.search(line)
			if result:
				print line




if __name__ == '__main__':
	print "Hello"



### Tests