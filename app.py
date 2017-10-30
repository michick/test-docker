#!/usr/bin/python

import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIR_TO_WATCH = '/var/impraise'

    def __init__(self):
        self.observer = Observer()

    def run(self):
        if not os.path.isdir(self.DIR_TO_WATCH):
            print('Specified path {} is not directory'.format(self.DIR_TO_WATCH))
            return
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIR_TO_WATCH, recursive=True)
        self.observer.start()

        try:
            while 1:
                time.sleep(1)
        except:
            self.observer.stop()
            print('Exiting')

        self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.event_type == 'created':
            type = 'directory' if event.is_directory else 'file'
            print('New {}: {}'.format(type, event.src_path.replace('/var/impraise', '/home/impraise/upload')))


if __name__ == '__main__':
    watcher = Watcher()
    watcher.run()
