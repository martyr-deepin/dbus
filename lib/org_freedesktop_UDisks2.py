#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbus

class DbusUDisks2:
    def __init__(self):
        self.dbus_name = 'org.freedesktop.UDisks2'
        self.dbus_path = '/org/freedesktop/UDisks2'
        self.dbus_ifc  = 'org.freedesktop.DBus.ObjectManager'

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_name,
                self.dbus_path)
        self.ifc_properties = dbus.Interface(self.system_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods = dbus.Interface(self.system_obj,
                dbus_interface=self.dbus_ifc)

    def GetManagedObjects(self):
        return self.ifc_methods.GetManagedObjects()
