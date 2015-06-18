#! python -tt
"""
Automate the boring stuff Chapter 9

https://automatetheboringstuff.com/chapter1/

"""

# import shutil, os, time
# import send2trash as trash

# filename = 'spam.txt'

# newfile = 'yum.txt'

# shutil.copy(filename, newfile)

# print 'moved'

# time.sleep(1)

# trash.send2trash(newfile)

# import os
# def walk():

# 	for folderName, subfolders, filenames in os.walk(os.getcwd()):
# 	    print('The current folder is ' + folderName)

# 	    for subfolder in subfolders:
# 	        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
# 	    for filename in filenames:
# 	        print('FILE INSIDE ' + folderName + ': '+ filename)

# 	    print('')

# import zipfile, os, send2trash, time

# os.chdir(os.getcwd())

# exampleZip = zipfile.ZipFile('example.zip')
# exampleZip.extractall()


# print exampleZip.namelist()

# time.sleep(1)

# send2trash.send2trash('cats/')

# print 'done'

# exampleZip.close()

# import zipfile, send2trash

# newZip = zipfile.ZipFile('new.zip', 'w')

# newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)

# newZip.close()

# send2trash.send2trash('new.zip')

import shutil, os, re

datePattern = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
       """, re.VERBOSE)


for filename in os.listdir('.'):
	mo = datePattern.search(filename)

	if mo == None:
		continue

	beforePart = mo.group(1)
	monthPart  = mo.group(2)
	dayPart    = mo.group(4)
	yearPart   = mo.group(6)
	afterPart  = mo.group(8)	

	print yearPart, monthPart, dayPart, '\n'








if __name__ == '__main__':
	print 'hello'

	assert 1 + 1 == 2

