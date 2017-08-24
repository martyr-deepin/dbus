#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbus

class DbusDisplay:
    def __init__(self):
        self.dbus_name = 'com.deepin.daemon.Display'
        self.dbus_path = '/com/deepin/daemon/Display'
        self.dbus_ifc  = 'com.deepin.daemon.Display'

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.dbus_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods = dbus.Interface(self.session_obj,
                dbus_interface=self.dbus_ifc)

    def getMonitors(self):
        """
        获取显示器列表Object Path
        """
        return self.ifc_properties.Get(self.dbus_ifc,
                "Monitors")

    def GetBrightness(self):
        """
        获取亮度值
        """
        return self.ifc_methods.GetBrightness()

    def SetBrightness(self, d_value):
        """
        设置亮度值
        """
        self.ifc_methods.SetBrightness(d_value)


class DbusDisplayMonitorVGA(object_path):
    def __init__(self):
        self.dbus_name = 'com.deepin.daemon.Display'
        self.dbus_path = object_path
        self.dbus_ifc  = 'com.deepin.daemon.Display.Monitor'

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.dbus_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods = dbus.Interface(self.session_obj,
                dbus_interface=self.dbus_ifc)

    def getModes(self):
        """
        获取显示器分辨率数组列表
        """
        return self.ifc_methods.Get(self.dbus_ifc,
                "Modes")
