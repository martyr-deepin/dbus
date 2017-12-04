#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbus
from gi.repository import GObject
from dbus.mainloop.glib import DBusGMainLoop

senders = ['com.deepin.dde.daemon.Dock']

def msg_cb(bus, msg):
    args = msg.get_args_list()
    print(args)

def signal_handler_DisplayModeChanged(bool_value, string_keystroke, string_3):
    """
    """
    if bool_value not in senders:
        return

    print("PropertiesChanged:", end=' ')
    print(bool_value, end=' | ')
    print(string_keystroke, end=' | ')
    print(string_3)

def signal_handler_EntryAdded(entryid, positon):
    print("EntryAdd: ", end=' ')
    print(entryid, end=' | ')
    print(positon)

if __name__ == '__main__':
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()

    #string = "type='signal', sender='com.deepin.dde.daemon.Dock', interface='org.freedesktop.DBus.Properties'"
    string = "type='signal', sender='com.deepin.dde.daemon.Dock',\
                            interface='com.deepin.dde.daemon.Dock'"
    bus.add_match_string(string)
    # bus.add_signal_receiver(signal_handler_DisplayModeChanged, signal_name="PropertiesChanged")
    bus.add_signal_receiver(signal_handler_EntryAdded, signal_name="EntryAdded")

    mainloop = GObject.MainLoop()
    mainloop.run()
