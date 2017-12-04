#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import dbus
import json
from gi.repository import GObject
from dbus.mainloop.glib import DBusGMainLoop

def signal_handler_EntryAdded(entryid, positon):
    with open('signal.txt', 'w') as f:
        f.write("DaemonDock|EntryAdded|%s|%s\n" % (entryid, positon))
        f.close()
        print("DaemonDock|EntryAdded|%s|%s\n" % (entryid, positon))

class SignalMonitorDaemonDock:
    def __init__(self):
        pass

    def run(self):
        DBusGMainLoop(set_as_default=True)
        bus = dbus.SessionBus()

        string = "type='signal', sender='com.deepin.dde.daemon.Dock',\
                            interface='com.deepin.dde.daemon.Dock'"
        bus.add_match_string(string)
        bus.add_signal_receiver(signal_handler_EntryAdded, signal_name="EntryAdded")

        mainloop = GObject.MainLoop()
        mainloop.run()

if __name__ == "__main__":
    monitor = SignalMonitorDaemonDock()
    monitor.run()
