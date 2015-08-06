import os
import shutil
import time

directory = '/projects/kulso_projektek/TEKINVEST_1501_LINUXECR/CI/dev-releases'
os.chdir(directory)
sortedList = sorted(os.listdir('.'), key=os.path.getctime)

oldDirectory = sortedList[0:(len(sortedList)-10)]
for old in oldDirectory:
	print ("Removed directory: " + os.path.join(directory, old, 'Product'))
#	shutil.rmtree(os.path.join(directory, old, 'Product'))