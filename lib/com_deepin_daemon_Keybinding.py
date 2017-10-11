#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import os
import dbus

class DbusKeybinding:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Keybinding"
        self.obj_path = "/com/deepin/daemon/Keybinding"
        self.interface = "com.deepin.daemon.Keybinding"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,

                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)

        self.NumLockState = "NumLockState"

    def getNumLockState(self):
        return self.ifc_properties.Get(self.interface,
                                       self.NumLockState)
    def List(self):
        return self.ifc_methods.List()

