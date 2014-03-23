#/bin/env python2
# encoding: utf8

from .backend.inotify import Flags
from . import main, on

@on(r'', dirs=None)
def default_task(ev):
    print 'event:', ev.path, ev.type, 'dir' if ev.is_dir else 'file'

@on(r'')
def file_task(ev):
    print 'file event:', ev.path

@on(r'', dirs=True)
def dir_task(ev):
    print 'dir event:', ev.path

main('.')
