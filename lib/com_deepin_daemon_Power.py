#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import os
import dbus

class DbusPower:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Power"
        self.obj_path = "/com/deepin/daemon/Power"
        self.interface = "com.deepin.daemon.Power"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,

                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)

        self.ScreenBlackLock = "ScreenBlackLock"
        self.SleepLock = "SleepLock"
        self.LinePowerScreenBlackDelay = "LinePowerScreenBlackDelay"
        self.LinePowerSleepDelay = "LinePowerSleepDelay"

    def getScreenBlackLock(self):
        return self.ifc_properties.Get(self.interface,
                                       self.ScreenBlackLock)

    def getSleepLock(self):
        return self.ifc_properties.Get(self.interface,
                                       self.SleepLock)

    def getLinePowerScreenBlackDelay(self):
        return self.ifc_properties.Get(self.interface,
                                       self.LinePowerScreenBlackDelay)

    def getLinePowerSleepDelay(self):
        return self.ifc_properties.Get(self.interface,
                                       self.LinePowerSleepDelay)
