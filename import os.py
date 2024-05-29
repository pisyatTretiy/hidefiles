import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MoveHandler(FileSystemEventHandler):
    def __init__(self, src_path, dest_path):
        self.src_path = src_path
        self.dest_path = dest_path

    def on_created(self, event):
        if not event.is_directory:
            file_name = os.path.basename(event.src_path)
            dest_file_path = os.path.join(self.dest_path, file_name)
            shutil.move(event.src_path, dest_file_path)
            print(f'Moved: {event.src_path} to {dest_file_path}')
if __name__ == "__main__":
    src_path = os.path.expanduser("~/Desktop")
    dest_path = os.path.expanduser("~/Documents/Hidden")

    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    
    event_handler = MoveHandler(src_path, dest_path)
    observer = Observer()
    observer.schedule(event_handler, src_path, recursive=False)
    observer.start()
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join() 
