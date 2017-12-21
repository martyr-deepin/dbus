#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import dbus
import json
from gi.repository import GObject
from dbus.mainloop.glib import DBusGMainLoop

def signal_handler_Added(wid):
    with open('signal.txt', 'w') as f:
        format_string = "TrayManager|Added|%d\n" % wid
        f.write(format_string)
        f.close()
        print(format_string, end="")

def signal_handler_Removed(wid):
    with open('signal.txt', 'w') as f:
        format_string = "TrayManager|Removed|%d\n" % wid
        f.write(format_string)
        f.close()
        print(format_string, end="")

class SignalMonitorTrayManager:
    def __init__(self):
        pass

    def run(self):
        DBusGMainLoop(set_as_default=True)
        bus = dbus.SessionBus()

        string = "type='signal', sender='com.deepin.dde.TrayManager',\
                            interface='com.deepin.dde.TrayManager'"
        bus.add_match_string(string)
        bus.add_signal_receiver(signal_handler_Added, signal_name="Added")
        bus.add_signal_receiver(signal_handler_Removed, signal_name="Removed")

        mainloop = GObject.MainLoop()
        mainloop.run()

if __name__ == "__main__":
    monitor = SignalMonitorTrayManager()
    monitor.run()
