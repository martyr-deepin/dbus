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
        return self.ifc_properties.Get(self.dbus_ifc,
                "DefaultEntry")

    def getEnableTheme(self):
        return self.ifc_properties.Get(self.dbus_ifc,
                "EnableTheme")

    def getResolution(self):
        return self.ifc_properties.Get(self.dbus_ifc,
                "Resolution")

    def getTimeout(self):
        return self.ifc_properties.Get(self.dbus_ifc,
                "Timeout")

    def getUpdating(self):
        return self.ifc_properties.Get(self.dbus_ifc,
                "Updating")

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


class DbusTheme:
    def __init__(self):
        self.dbus_name = 'com.deepin.daemon.Grub2'
        self.dbus_path = '/com/deepin/daemon/Grub2/Theme'
        self.dbus_ifc  = 'com.deepin.daemon.Grub2.Theme'

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_name,
                self.dbus_path)
        self.ifc_properties = dbus.Interface(self.system_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods = dbus.Interface(self.system_obj,
                dbus_interface=self.dbus_ifc)

    def getUpdating(self):
        return self.ifc_properties.Get(self.dbus_ifc,
                "Updating")

    def getItemColor(self):
        return self.ifc_properties.Get(self.dbus_ifc,
                "ItemColor")

    def getSelectedItemColor(self):
        return self.ifc_properties.Get(self.dbus_ifc,
                "SelectedItemColor")

    def GetBackground(self):
        return self.ifc_methods.GetBackground()

    def SetBackgroundSourceFile(self, newFilePath):
        return self.ifc_methods.SetBackgroundSourceFile(newFilePath)

    def SetItemColor(self, newColor):
        return self.ifc_methods.SetItemColor(newColor)

    def SetSelectedColor(self, newColor):
        return self.ifc_methods.SetSelectedColor(newColor)
