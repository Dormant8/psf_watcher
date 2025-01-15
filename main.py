import time
from shutil import copyfile
from sys import argv as argv
from subprocess import run

from keyboard import is_pressed
from watchdog.events import FileSystemEvent, FileSystemEventHandler, FileModifiedEvent
from watchdog.observers import Observer

class MyEventHandler(FileSystemEventHandler):
    def on_modified(self, event: FileModifiedEvent):
        # ~ check is for VIM's temporary file used to overwrite source on save
        if event.event_type == "modified" and not '~' in event.src_path and not event.is_directory: 
            target_file = event.src_path
            target_file = target_file.replace(TARGET_DIR, '')
            if TARGET_DIR in event.src_path:
                # Clean up this print : consider adding the time of print as well.
                print("~~~~~~~~~~~~~~~")
                print("Copying started")
                print("     src_path: " + event.src_path)
                print("     copy dir: " + COPY_TO_DIR)
                print("     target_dir: " + TARGET_DIR)
                print("     file name: " + target_file)
                print("~~~~~~~~~~~~~~~")
                copyfile(event.src_path, COPY_TO_DIR + target_file)

            if PDF_DIR in event.src_path:  # TODO : returnt o make this work
                if ".pdf" in target_file:
                    print("~~~~~~~~~~~~~~~")
                    print("Opening PDF started")
                    print("     pdf dir: " + PDF_DIR)
                    print("     file name: " + target_file)
                    print("~~~~~~~~~~~~~~~")
                    run(["Acrobat", target_file]) # make sure this runs the most recent pdf

# ~~~~~~~~~~~~~~~~~~~~ END CLASS MyEventHandler
if not len(argv) in [3, 4, 5]: # TODO : Change s.t. there are only two options (remove 3).  only optional one is specifying the sleep time
    print("Wrong number of args")
    exit()

print("Running: " + argv[0])
print("Num args: " + str(len(argv)))
print("Target/Watched Directory: " + argv[1])
TARGET_DIR = ".\\" + argv[1]
print("Distiller In/Copy To Directory: " + argv[2])
COPY_TO_DIR = ".\\" + argv[2]
print("Distiller out/PDF Directory" + argv[3])
PDF_DIR = ".\\" + argv[3]
# We also want to watch for the pdf as it is created
seconds_sleep = 1
if(len(argv) == 5):
    seconds_sleep = argv[4]

event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, ".", recursive=True)
observer.start()

print("Hold 'q' to quit")
#The reason you have to hold is that this check only happens once per sleep cycle
try:
    while not is_pressed('q'): 
        time.sleep(int(seconds_sleep))
finally:
    observer.stop()
    observer.join()
