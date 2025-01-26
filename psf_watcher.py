import time
from shutil import copyfile
from sys import argv as argv
from subprocess import run
from os.path import abspath as abspath

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

            if PDF_DIR in event.src_path and ".pdf" in event.src_path:
                    #run(["Acrobat", event.src_path]) # TODO : swap comments
                    #run(["Acrobat", target_file]) 
                    print("Opening PDF started")
                    print("     file name: " + event.src_path)
                    print("     dupe check name: " + target_file)


# ~~~~~~~~~~~~~~~~~~~~ END CLASS MyEventHandler
# ~~~~~~~~~~~~~~~~~~~~ Script
if not len(argv) in [2, 3]:
    print("Wrong number of args")
    exit()

# watchdog objects
event_handler = MyEventHandler()
observer = Observer()


ABS_PATH = abspath(__file__).removesuffix(argv[0]) # gets path to script
print(ABS_PATH)
TARGET_DIR = str(argv[1])
DISTILLER_DIR = str(argv[2])

sleep_seconds = 1
if len(argv) == 3 and argv[2].isnumeric():
    sleep_seconds = float(argv[2])

paths = [TARGET_DIR, DISTILLER_DIR]

for idx, path in enumerate(paths):
    if path.startswith(".\\") or path.startswith("./"):
        path = path[2:]
    if path.endswith("\\") or path.endswith("/"):
        path = path[:-1]
    paths[idx] = ABS_PATH + path

TARGET_DIR = paths[0]
DISTILLER_DIR = paths[1]

COPY_TO_DIR = DISTILLER_DIR + "\\in"
PDF_DIR = DISTILLER_DIR + "\\out"

for dir in [TARGET_DIR, COPY_TO_DIR, PDF_DIR]:
    print("Scheduling " + dir)
    observer.schedule(event_handler, dir)


print("Starting:            " + argv[0])
print("Working psfs:        " + TARGET_DIR)
print("Distiller Directory: " + DISTILLER_DIR)
print()
print('Press "Ctr+C" to exit')

observer.start()

#The reason you have to hold is that this check only happens once per sleep cycle
#not a good choice with sleep call
try:
    while True: 
        #observer checks here
        time.sleep(sleep_seconds)
except KeyboardInterrupt:
    pass
finally:
    print("Exiting program")
    observer.stop()
    observer.join()
