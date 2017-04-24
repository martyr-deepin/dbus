#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbus

class DbusGrub2:
    def __init__(self):
        self.dbus_name = 'com.deepin.daemon.Grub2'
        self.dbus_path = '/com/deepin/daemon/Grub2'
        self.dbus_ifc  = 'com.deepin.daemon.Grub2'

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_name,
                self.dbus_path)
        self.ifc_properties = dbus.Interface(self.system_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods = dbus.Interface(self.system_obj,
                dbus_interface=self.dbus_ifc)

    def getDefaultEntry(self):
        return self.ifc_properties.DefaultEntry("DefaultEntry")

    def getEnableTheme(self):
        return self.ifc_properties.DefaultEntry("EnableTheme")

    def getResolution(self):
        return self.ifc_properties.DefaultEntry("Resolution")

    def getTimeout(self):
        return self.ifc_properties.DefaultEntry("Timeout")

    def getUpdating(self):
        return self.ifc_properties.DefaultEntry("Updating")

    def GetAvailableResolutions(self):
        """
        [{"Text":"Auto","Value":"auto"},{"Text":"1024x768","Value":"1024x768"},{"Text":"800x600","Value":"800x600"}]
        """
        return self.ifc_methods.GetAvailableResolutions()

    def GetSimpleEntryTitles(self):
        return self.ifc_methods.GetSimpleEntryTitles()

    def SetDefaultEntry(self, newEntry):
        """
        newEntry: type string Entry name
        """
        return self.ifc_methods.SetDefaultEntry(newEntry)

    def SetEnableTheme(self, newTheme):
        """
        newTheme: type bool True or False
        """
        return self.ifc_methods.SetEnableTheme(newTheme)

    def SetResolution(self, newResolution):
        return self.ifc_methods.SetResolution(newResolution)

    def SetTimeout(self, newTimeout):
        """
        newTimeout: type int seconds
        """
        return self.ifc_methods.SetTimeout(newTimeout)
