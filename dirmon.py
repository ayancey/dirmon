import os
import time

class DirectoryMonitor:
	directory = ''
	interval = 0
	on_added = None
	on_removed = None
	loop = False

	def __init__(self, path, interval):
		self.directory = path
		self.interval = interval

	def start(self):
		self.loop = True

		# The first before output is run outside of the loop
		before = os.listdir(self.directory)
		while self.loop:
			time.sleep(self.interval)	
			after = os.listdir(self.directory)

			# Compares lists and passes file/folder names
			removed = list(set(before) - set(after))
			for file in removed:
				if self.on_removed:
					self.on_removed(file)

			added = list(set(after) - set(before))
			for file in added:
				if self.on_added:
					self.on_added(file)

			# Uses after output for the next before output
			before = after

	def stop(self):
		self.loop = False
