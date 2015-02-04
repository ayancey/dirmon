import os
import time


class DirectoryMonitor:
	directory = ''
	interval = 0
	on_added = None
	on_removed = None
	loop = 1

	def __init__(self, path_i, interval_i):
		self.directory = path_i
		self.interval = interval_i

	def start(self):
		self.loop = 1
		while self.loop == 1:
			before = os.listdir(self.directory)

			time.sleep(self.interval)

			after = os.listdir(self.directory)

			for file in before:
				pass
				#`print file

			removed = list(set(before) - set(after))
			for file in removed:
				if not self.on_removed == None:
					self.on_removed(file)

			added = list(set(after) - set(before))
			for file in added:
				if not self.on_added == None:
					self.on_added(file)

	def stop(self):
		self.loop = 0

this = DirectoryMonitor('C:\Users\Alex\Downloads',1)

def ohman(thefile):
	print 'Added: ' + thefile
	this.stop()
	this.directory = 'C:\\'
	this.start()

def ohman2(thefile):
	print 'Removed: ' + thefile


this.on_added = ohman
this.on_removed = ohman2
this.start()

