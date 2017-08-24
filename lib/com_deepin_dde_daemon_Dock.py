#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import dbus
from time import sleep

class DaemonDock:
    def __init__(self):
        self.dbus_name = "com.deepin.dde.daemon.Dock"
        self.obj_path  = "/com/deepin/dde/daemon/Dock"
        self.interface = "com.deepin.dde.daemon.Dock"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)

    def getDockedApps(self):
        return self.ifc_properties.Get(self.interface,
                "DockedApps")

    def getFrontendWindowRect(self):
        return self.ifc_properties.Get(self.interface,
                "FrontendWindowRect")

    def getDisplayMode(self):
        return self.ifc_properties.Get(self.interface,
                "DisplayMode")

    def getPosition(self):
        return self.ifc_properties.Get(self.interface,
                "Position")

    def getIconSize(self):
        return self.ifc_properties.Get(self.interface,
                "IconSize")

    def getHideMode(self):
        return self.ifc_properties.Get(self.interface,
                "HideMode")

    def getHideState(self):
        return self.ifc_properties.Get(self.interface,
                "HideState")

    def setDisplayMode(self, mode):
        self.ifc_properties.Set(self.interface,
                "DisplayMode", mode)
        sleep(2)

    def setPosition(self, direction):
        self.ifc_properties.Set(self.interface,
                "Position", direction)
        sleep(2)

    def setIconSize(self, direction):
        self.ifc_properties.Set(self.interface,
                "IconSize", direction)
        sleep(2)

    def setHideMode(self, direction):
        self.ifc_properties.Set(self.interface,
                "HideMode", direction)
        sleep(2)

