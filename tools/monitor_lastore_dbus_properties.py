#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbus
from gi.repository import GObject
from dbus.mainloop.glib import DBusGMainLoop

senders = ['com.deepin.lastore.Job',
           'com.deepin.lastore.Manager',
           'com.deepin.lastore.Updater']

def signal_handler_DisplayModeChanged(bool_value, string_keystroke, string_3):
    if bool_value not in senders:
        return

    print("PropertiesChanged:", end=' ')
    print(bool_value, end=' | ')
    print(string_keystroke, end=' | ')
    print(string_3)

if __name__ == '__main__':
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SystemBus()

    #string = "type='signal', sender='com.deepin.lastore', interface='com.deepin.lastore.Manager'"
    #string = "type='signal', sender='com.deepin.lastore'"
    #bus.add_match_string(string)
    bus.add_signal_receiver(signal_handler_DisplayModeChanged, signal_name="PropertiesChanged")

    mainloop = GObject.MainLoop()
    mainloop.run()
