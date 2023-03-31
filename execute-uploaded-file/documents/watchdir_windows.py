import sys
import time
import logging
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import LoggingEventHandler
import os
import shlex

#Customizing FileSystemEventHandler from watchdogn 
#on_created is a watchdog endpoint. 

class CommandExecutionHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:

            path = str(event.src_path)
           
            if "/.~" in path:
                return 


            #Nest in a Try/Except to try mutiple differnet executions
            print("New file added to directory: "+ str(event.src_path))

          


            #Attempting to execute file
            #subprocess.run(event.src_path, shell=True)

            #LibreOffice Command 
            filename = str(os.path.basename(event.src_path))
            print(filename)
            command = "soffice " + filename
            
            print("Executing command: " + command)
            cmd = subprocess.Popen('cmd.exe /K ' + command)
            #os.system("start cmd /c" + command)
            
            time.sleep(25)
           
            subprocess.call(['taskkill', '/F', '/IM', 'soffice.bin'])
            subprocess.Popen('cmd.exe /K del ' + filename )

            
            subprocess.call(['taskkill', '/F', '/IM', 'cmd.exe'])
         

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
