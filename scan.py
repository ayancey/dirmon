import os
import time

before = os.listdir('C:\Users\Alex\Downloads')

for file in before:
	print file

time.sleep(1)

after = os.listdir('C:\Users\Alex\Downloads')

for file in before:
	print file