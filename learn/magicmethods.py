#!/usr/bin/env python 

"""
Learning about python magic methods


http://www.rafekettler.com/magicmethods.html

author : nathanjdanielsen [at] gmail.com

"""


from os.path import join

class FileObject:
	"""
	Wrapper for file objects to make sure the file gets closed on deletion.
	"""
	def __init__(self, filepath='~', filename='sample.txt'):
		#open a file filename in filepath in read and write mode
		self.file = open(join(filepath, filename), 'r+')

	def __del__(self):
		self.file.close()
		del self.file


class Word(str):
	"""
	Class for words, defining comparison based on word length
	"""

	def __new__(cls, word):
		#note that we have use __new__. This is because str is an immutable 
		#type, so we have to initalize it early (at creation time)

		if " " in word:
			print "Value contains space. Truncating to first space"
			word = word[:word.index(' ')]

		return str.__new__(cls, word)

	def __gt__(self, other):
		return len(self) > len(other)

	def __lt__(self, other):
		return len(self) < len(other)

	def __ge__(self, other):
		return len(self) >= len(other)

	def __le__(self, other):
		return len(self) <= len(other)








if __name__ == "__main__":

	print "hello"


	word1, word2 =  Word("gibberish"), Word("One")


	#word3 = Word("Something s")

	print word1 > word2