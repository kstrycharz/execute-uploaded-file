import sys
import time
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import LoggingEventHandler
import os

#Customizing FileSystemEventHandler from watchdogn 
#on_created is a watchdog endpoint. 

class CommandExecutionHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
           
            #Nest in a Try/Except to try mutiple differnet executions
            print("New file added to directory: "+ str(event.src_path))

            #Attempting to execute file
            #subprocess.run(event.src_path, shell=True)

            #LibreOffice Command 
            filename = "'" + str(event.src_path) + "'"


            command = 'echo libreoffice ' + filename 
            print("Executing command: " + command  )
            os.system(command)
            

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    
   
    
    #event_handler = LoggingEventHandler()
    event_handler = CommandExecutionHandler()



    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()


    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
