#/bin/env python2
# encoding: utf8

from .backend.inotify import Flags
from . import main, on_event

#@on_event(r'^(.*/)*?[^.]')
@on_event(r'')
def muhtask(ev):
    #print 'event:', ev.wd, ev.path, Flags(ev.mask)
    print 'event:', ev.path, ev.type, 'dir' if ev.is_dir else 'file'

main('.')
