#! venv/bin/python

# import the modules
import sys
import time
import logging
import subprocess
from watchdog.observers import Observer
#from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler

class CSVHandler(FileSystemEventHandler):
    def __init__(self, logging):
        self.logging = logging

    def on_any_event(self, event):
        self.logging.info("%s %s", event.event_type, event.src_path)

    def on_created(self, event):
        #print(event.src_path.strip())
        if (event.src_path).endswith('.csv'):
            print(f'Found {event.src_path}')


if __name__ == "__main__":
	# Set the format for logging info
	logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

	# Set format for displaying path
	path = sys.argv[1] if len(sys.argv) > 1 else '.'

	# Initialize logging event handler
	#event_handler = CSVHandler(path)
	event_handler = CSVHandler(logging)

	# Initialize Observer
	observer = Observer()
	observer.schedule(event_handler, path, recursive=True) # it seems that recursive must be set to True

	# Start the observer
	observer.start()
	try:
		while True:
			# Set the thread sleep time
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()
