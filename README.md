# dirmon
Barebones cross-platform library for detecting files added and removed from a directory.

# Example
```python
from dirmon import DirectoryMonitor

# Class DirectoryMonitor("PATH", SCAN INTERVAL [in seconds])
monitor = DirectoryMonitor(".", 5)

def added(file):
	print('Added: ' + file)
	if file == ".git":
		print("Git initiated")
		monitor.stop()

def removed(file):
	print('Removed: ' + file)

monitor.on_added = added
monitor.on_removed = removed
monitor.start()
```
