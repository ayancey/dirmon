import os
import time

class DirectoryMonitor:
	directory = ''
	interval = 0
	loop = 0
	on_added = None
	on_removed = None
	before = None

	def __init__(self, path, interval):
		self.directory = path
		self.interval = interval

	def start(self):
		self.loop = True
		while self.loop:
			# Polls the directory twice for the first iteration
			if not self.before:
				self.before = os.listdir(self.directory)
				time.sleep(self.interval)
				
			after = os.listdir(self.directory)

			# Compares lists and passes file/folder names
			removed = list(set(self.before) - set(after))
			for file in removed:
				if self.on_removed:
					self.on_removed(file)

			added = list(set(after) - set(self.before))
			for file in added:
				if self.on_added:
					self.on_added(file)

			# Uses after output for the next before output
			self.before = after
			time.sleep(self.interval)

	def stop(self):
		self.loop = False
