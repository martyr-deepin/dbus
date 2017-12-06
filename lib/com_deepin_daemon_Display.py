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
        获取显示器列表Object Path，以Primary主屏名结尾的是主显示器
        """
        return self.ifc_properties.Get(self.dbus_ifc,
                                       "Monitors")

    def getPrimary(self):
        """
        获取主屏名
        """
        return self.ifc_properties.Get(self.dbus_ifc,
                                       "Primary")

    def ApplyChanges(self):
        """
        修改旋转屏幕显示后，需要刷新屏幕显示，使设置生效
        """
        try:
            self.ifc_methods.ApplyChanges()
            return True
        except Exception as e:
            print("Unexpected Error: {}".format(e))
            return False

    def GetBrightness(self):
        """
        获取各显示器亮度值
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
        return self.ifc_properties.Get(self.dbus_ifc,
                "Modes")

    def getRotations(self):
        """
        获取旋转取值列表, [1, 2, 4, 8]
        """
        return self.ifc_properties.Get(self.dbus_ifc,
                "Rotations")

    def SetRotation(self, rotation):
        """
        设置屏幕旋转
            1 正常
            2 逆时针旋转90°
            4 逆时针旋转180°
            8 逆时针旋转270°
        """
        try:
            self.ifc_methods.SetRotation(rotation)
            return True
        except Exception as e:
            print("Unexpected Error: {}".format(e))
            return False
