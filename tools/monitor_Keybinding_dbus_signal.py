#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbus
from gi.repository import GObject
from dbus.mainloop.glib import DBusGMainLoop

def msg_cb(bus, msg):
    args = msg.get_args_list()
    print(args)

def signal_handler_KeyEvent(bool_value, string_keystroke):
    """
    信号KeyEvent回调函数：
        bool_value: True表示按键，False表示松开按键
        string_keystroke: 显示组合件keystroke

        KeyEvent: 1, <Control><Alt>grave
        KeyEvent: 0, <Control><Alt>grave
    """
    if bool_value:
        return

    print("KeyEvent:", end=' ')
    print(bool_value, end=', ')
    print(string_keystroke)

def signal_handler_Added(string_name, int_type):
    """
    信号Added回调函数：
        string_id:  快捷键id值，长度32
        int_type:   快捷键type值
    """
    print(string_name, end=',')
    print(int_32)

if __name__ == '__main__':
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()

    string = "type='signal',sender='com.deepin.daemon.Keybinding',interface='com.deepin.daemon.Keybinding'"
    bus.add_match_string(string)
    #bus.add_message_filter(msg_cb)
    bus.add_signal_receiver(signal_handler_KeyEvent, signal_name="KeyEvent")
    bus.add_signal_receiver(signal_handler_Added, signal_name="Added")

    mainloop = GObject.MainLoop()
    mainloop.run()
