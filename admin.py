#!/usr/bin/env python 

"""
Control center for python excercises that I am working on. 

"""

### Builtins
import tests


### Modules
from learn.learnre import RE



### Main

class Controller(RE):
	def __init__(self, file):
		self.file = open(file, "r")
		pass

	def main(self):
		"""
		Confirms that the file is open and the instance is created.
		"""
		print self.initprint()

	def findlog(self):
		pattern = "^RUN\ (\d{6})\ COMPLETED.\ OUTPUT\ IN\ FILE\ ([a-z]+.dat)\.$"
		return self.research(pattern)

	def grouplog(self):
		pattern = "^RUN\ (\d{6})\ COMPLETED.\ OUTPUT\ IN\ FILE\ ([a-z]+.dat)\.$"
		return self.research(pattern)

	def messages(self):
		"""
		Uses regex to parse a string like this:
		Jun 25 00:20:13 noether syslog-ng[2298]: STATS: dropped 0

		Jun 25 23:47:33 noether sshd[9277]: Invalid user account from 207.54.140.124	
		"""	
		pattern = r'^[A-Z][a-z]{2} [123 ][0-9] \d\d:\d\d:\d\d noether sshd\[\d+\]: Invalid user \S+ from \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$' 
		return self.research(pattern)

	def month(self):
		"""
		Uses regex verbose mode to parse a string like this:
		Jun 25 00:20:13 noether syslog-ng[2298]: STATS: dropped 0

		Jun 25 23:47:33 noether sshd[9277]: Invalid user account from 207.54.140.124	
		"""	
		pattern =  r'''
			^
			(Jan|Feb|Mar|Apr|Jul)\ 				# Month
			[123 ][0-9]\ 						# Day
			\d\d:\d\d:\d\d\ 					# Time
			noether\ 
			sshd\[\d+\]:\ 						# Process ID
			Invalid\ user\ 
			\S+\ 								# User ID
			from\ 
			\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} 	# IP Address
			$
			'''
		return self.verb_research(pattern)


### Tests

if __name__ == '__main__':
	tester = Controller("docs/log.txt")
	# tester.initprint()
	tester.grouplog()

	# logger = Controller("docs/messages.txt")
	# logger.initprint()
	# logger.month()