#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import dbus

class DbusTrayManager:
    def __init__(self):
        self.dbus_name = "com.deepin.dde.TrayManager"
        self.dbus_path  = "/com/deepin/dde/TrayManager"
        self.dbus_ifc = "com.deepin.dde.TrayManager"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.dbus_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.dbus_ifc)

    def getTrayIcons(self):
        return self.ifc_properties.Get(self.dbus_ifc,
                "TrayIcons")

    def EnableNotification(self, xid, value):
        return self.ifc_methods.EnableNotification(xid, value)

    def GetName(self, xid):
        return self.ifc_methods.GetName(xid)
