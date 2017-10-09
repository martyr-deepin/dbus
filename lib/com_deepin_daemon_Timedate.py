#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import os
import dbus

class DbusTimedate:
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

    def AddUserTimezone(self, timezone):
        self.ifc_methods.AddUserTimezone(timezone)

    def DeleteUserTimezone(self, timezone):
        self.ifc_methods.DeleteUserTimezone(timezone)

    def GetZoneInfo(self, timezone):
        return self.ifc_methods.GetZoneInfo(timezone)

    def GetZoneList(self):
        return self.ifc_methods.GetZoneList()

    def SetDate(self, year, month, day, hour, minute):
        self.ifc_methods.SetDate(year, month, day, hour, minute, 0, 0)

    def SetNTP(self, setbool):
        self.ifc_methods.SetNTP(setbool)

    def SetTimezone(self, zoneinfo):
        self.ifc_methods.SetTimezone(zoneinfo)

    def getUserTimezones(self):
        return self.ifc_properties.Get(self.interface,
                self.UserTimezones)

    def getCanNTP(self):
        return self.ifc_properties.Get(self.interface,
                self.CanNTP)

    def getLocalRTC(self):
        return self.ifc_properties.Get(self.interface,
                self.LocalRTC)

    def getNTP(self):
        return self.ifc_properties.Get(self.interface,
                self.NTP)

    def getUse24HourFormat(self):
        return self.ifc_properties.Get(self.interface,
                self.Use24HourFormat)

    def getDSTOffset(self):
        return self.ifc_properties.Get(self.interface,
                self.DSTOffset)

    def getTimezone(self):
        return self.ifc_properties.Get(self.interface,
                self.Timezone)
