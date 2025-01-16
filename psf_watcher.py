import time
from shutil import copyfile
from sys import argv as argv
from subprocess import run
from os import path.abspath as abspath

from keyboard import is_pressed
from watchdog.events import FileSystemEventHandler, FileModifiedEvent
from watchdog.observers import Observer

class MyEventHandler(FileSystemEventHandler):
    def on_modified(self, event: FileModifiedEvent):
        # ~ check is for VIM's temporary file used to overwrite source on save
        if event.event_type == "modified" and not '~' in event.src_path and not event.is_directory: 
            target_file = event.src_path
            target_file = target_file.replace(TARGET_DIR, '')
            if TARGET_DIR in event.src_path:
                copyfile(event.src_path, COPY_TO_DIR + target_file)
                print("Copy complete") # TODO : comment
                print("     src_path:    " + event.src_path)
                print("     copy to dir: " + COPY_TO_DIR)
                print("     target_dir:  " + TARGET_DIR)
                print("     file name:   " + target_file)

            if PDF_DIR in event.src_path:
                if ".pdf" in target_file:
                    #run(["Acrobat", target_file]) # TODO : swap comments
                    print("Opening PDF started")
                    print("     file name: " + target_file)

# ~~~~~~~~~~~~~~~~~~~~ END CLASS MyEventHandler
# ~~~~~~~~~~~~~~~~~~~~ Script
if not len(argv) in [2, 3]:
    print("Wrong number of args")
    exit()


event_handler = MyEventHandler()
observer = Observer()

print("Running:             " + argv[0])
print("Working psfs:        " + argv[1])
print("Distiller Directory: " + argv[2])

ABS_PATH = abspath(__file__) # gets path to script
TARGET_DIR = argv[1]
COPY_TO_DIR = argv[2] + "\\in"
PDF_DIR = argv[2] + "\\out"

sleep_seconds = 1
if len(argv) == 3 and argv[3].isnumeric():
    sleep_seconds = int(argv[3])

for dir in [TARGET_DIR, COPY_TO_DIR, PDF_DIR]:
    if dir.startswith(".\\"):
        dir = ABS_PATH + dir[1:]
    observer.schedule(event_handler, dir)

observer.start()

print("Hold 'q' to quit")
#The reason you have to hold is that this check only happens once per sleep cycle
#not a good choice with sleep call
try:
    while not is_pressed('q'): 
        time.sleep(int(seconds_sleep))
finally:
    observer.stop()
    observer.join()
