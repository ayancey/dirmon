import os
import time

class DirectoryMonitor:
	directory = ''
	interval = 0
	on_added = None
	on_removed = None

	def __init__(self, path_i, interval_i):
		self.directory = path_i
		self.interval = interval_i

	def start(self):
		before = os.listdir(self.directory)

		time.sleep(self.interval)

		after = os.listdir(self.directory)

		for file in before:
			pass
			#`print file

		removed = list(set(before) - set(after))
		for file in removed:
			self.on_removed(file)

		added = list(set(after) - set(before))
		for file in added:
			self.on_added(file)

def ohman(thefile):
	print 'Added: ' + thefile

def ohman2(thefile):
	print 'Removed: ' + thefile

this = DirectoryMonitor('C:\Users\Alex\Downloads')
this.on_added = ohman
this.on_removed = ohman2
this.start()

