import os
import time

before = os.listdir('C:\Users\Alex\Downloads')

for file in before:
	print file

print '----------------'
time.sleep(5)

after = os.listdir('C:\Users\Alex\Downloads')

for file in before:
	print file

removed = list(set(before) - set(after))

print 'REMOVED:'
print '------------'
for file in removed:
	print file

added = list(set(after) - set(before))

print 'ADDED:'
print '------------'
for file in added:
	print file
