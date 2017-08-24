#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import dbus

class DbusNetwork:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Network"
        self.obj_path  = "/com/deepin/daemon/Network"
        self.interface = "com.deepin.daemon.Network"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)

    def getNetworkingEnabled(self):
        return self.ifc_properties.Get(self.interface,
                "NetworkingEnabled")

    def getVpnEnabled(self):
        return self.ifc_properties.Get(self.interface,
                "VpnEnabled")

    def getActiveConnections(self):
        return self.ifc_properties.Get(self.interface,
                "getActiveConnections")

    def getConnections(self):
        return self.ifc_properties.Get(self.interface,
                "Connections")

    def getDevices(self):
        return self.ifc_properties.Get(self.interface,
                "Devices")

    def getState(self):
        return self.ifc_properties.Get(self.interface,
                "State")

    def GetActiveConnectionInfo(self):
        return self.ifc_methods.GetActiveConnectionInfo()
