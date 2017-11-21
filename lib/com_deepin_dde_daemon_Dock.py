#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import dbus
from time import sleep

class DbusDaemonDock:
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


    def ActivateWindow(self, winId):
        """
        激活给定id的窗口，被激活的窗口通常成为焦点窗口
        """
        return self.ifc_methods.ActivateWindow(winId)

    def CancelPreviewWindow(self):
        """
        取消dock预览窗口
        """
        return self.ifc_methods.CancelPreviewWindow()

    def CloseWindow(self, winId):
        """
        将传入winId的窗口关闭
        """
        return self.ifc_methods.CloseWindow(winId)

    def GetEntryIDs(self):
        """
        获取驻留在dock中应用的Object path
        """
        return self.ifc_methods.GetEntryIDs()

    def IsDocked(self, desktopFilePath):
        """
        判断是否驻留在dock上
        入参：
            desktopFilePath：   '/usr/share/applications/d-feet.desktop'
        """
        return self.ifc_methods.IsDocked(desktopFilePath)

    def IsOnDock(self, desktopFilePath):
        """
        判断是否显示在dock上
        入参：
            desktopFilePath：   '/usr/share/applications/d-feet.desktop'
        """
        return self.ifc_methods.IsOnDock(desktopFilePath)

    def MakeWindowAbove(self, winId):
        return self.ifc_methods.MakeWindowAbove(winId)

    def MaximizeWindow(self, winId):
        """
        将传入winId的窗口最大化
        """
        return self.ifc_methods.MaximizeWindow(winId)

    def MinimizeWindow(self, winId):
        """
        将传入winId的窗口最小化
        """
        return self.ifc_methods.MinimizeWindow(winId)

    def MoveEntry(self, num1, num2):
        """
        驻留应用位置交换，从启动器之后位置从0开始计算，可通过查看GetEntryIDs查看交换结果
        """
        return self.ifc_methods.MoveEntry(num1, num2)

    def MoveWindow(self, winId):
        return self.ifc_methods.MoveWindow(winId)

    def PreviewWindow(self, winId):
        """
        预览窗口
        """
        return self.ifc_methods.PreviewWindow(winId)

    def QueryWindowIdentifyMethod(self, winId):
        """
        winInfo identifyMethod
        """
        return self.ifc_methods.QueryWindowIdentifyMethod(winId)

    def RequestDock(self, desktopFilePath, num):
        """
        驻留到dock上
        入参：
            desktopFilePath:    desktopFilePath全路径
            num:    在dock上的位置
        """
        return self.ifc_methods.RequestDock(desktopFilePath, num)

    def RequestUndock(self, desktopFilePath):
        """
        取消驻留
        """
        return self.ifc_methods.RequestUndock(desktopFilePath)

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

