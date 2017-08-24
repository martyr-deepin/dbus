#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import dbus

class Lock:
    def __init__(self):
        self.dbus_name = "com.deepin.dde.lock"
        self.obj_path  = "/com/deepin/dde/lock"
        self.interface = "com.deepin.dde.lock"

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.system_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.system_obj,
                dbus_interface=self.interface)

    def UnlockCheck(self, username, password):
        return self.ifc_methods.UnlockCheck(username, password)

    def CurrentUser(self):
        return self.ifc_methods.CurrentUser()
