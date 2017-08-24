#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import os
import dbus

class Timedate:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Timedate"
        self.obj_path = "/com/deepin/daemon/Timedate"
        self.interface = "com.deepin.daemon.Timedate"

        self.UserTimezones = 'UserTimezones'
        self.CanNTP = 'CanNTP'
        self.LocalRTC = 'LocalRTC'
        self.NTP = 'NTP'
        self.Use24HourFormat = 'Use24HourFormat'
        self.DSTOffset = 'DSTOffset'
        self.Timezone = 'Timezone'


        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,

                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)

    def SetNTP(self, setbool):
        self.ifc_methods.SetNTP(setbool)

    def GetZoneList(self):
        return self.ifc_methods.GetZoneList()

    def SetTimezone(self, zoneinfo):
        self.ifc_methods.SetTimezone(zoneinfo)

    def getUserTimezones(self):
        return self.ifc_properties.Get(self.interface,
                self.UserTimezones)

    def getCanNTP(self):
        return self.ifc_properties.Get(self.interface,
                self.CanNTP)

    def getTimezone(self):
        return self.ifc_properties.Get(self.interface,
                self.Timezone)

    def getUse24HourFormat(self):
        return self.ifc_properties.Get(self.interface,
                self.Use24HourFormat)

    def getNTP(self):
        return self.ifc_properties.Get(self.interface,
                self.NTP)
