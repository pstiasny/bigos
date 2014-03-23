#/bin/env python2
# encoding: utf8

import re
import itertools

#from .backend.inotify import generate_events
from .backend.polling import generate_events

watchlist = []

class EventHandler:
    def __init__(self, function, regex, dirs=False):
        '''
        :param function: function to run when the event is matched
        :param regex:    regular expression string to match the
                         path against
        :param dirs:     should the handler be run for directory events,
                         None to run for both dirs and files
        '''
        self.f = function
        self.regex = re.compile(regex)
        self.dirs = dirs

    def match(self, ev):
        dir_match = self.dirs is None or (ev.is_dir == self.dirs)
        return dir_match and self.regex.match(ev.path)

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

def on(*args, **kwargs):
    def decorate(f):
        watchlist.append(EventHandler(f, *args, **kwargs))
        return f
    return decorate

def handle_event(watchlist, ev):
    for handler in watchlist:
        if handler.match(ev):
            handler(ev)

def main(dirpath, watchlist=watchlist):
    for ev in itertools.chain.from_iterable(generate_events(dirpath)):
        handle_event(watchlist, ev)

