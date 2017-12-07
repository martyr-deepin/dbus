#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import dbus
from time import sleep

class DbusDaemonLauncher:
    def __init__(self):
        self.dbus_name = "com.deepin.dde.daemon.Launcher"
        self.obj_path  = "/com/deepin/dde/daemon/Launcher"
        self.interface = "com.deepin.dde.daemon.Launcher"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)


    def GetAllItemInfos(self):
        """
        获取launcher中所有item
        """
        return self.ifc_methods.GetAllItemInfos()

    def GetAllNewInstalledApps(self):
        """
        获取新安装的应用名
        """
        return self.ifc_methods.GetAllNewInstalledApps()

    def GetItemInfo(self, app_name):
        """
        获取应用的相关信息
        ('/usr/share/applications/deepin-terminal.desktop',
        '深度终端',
        'deepin-terminal',
        'deepin-terminal',
        9,
        0)
        """
        return self.ifc_methods.GetItemInfo(app_name)

    def IsItemOnDesktop(self, app_name):
        """
        应用desktop文件是否在桌面
        """
        return self.ifc_methods.IsItemOnDesktop(app_name)

    def MarkLaunched(self, app_name):
        """
        launcher中标记新安装的应用，去掉显示小蓝点，从AllNewInstalledApps中移除
        需要再次调用GetAllNewInstalledApps再次确认
        """
        try:
            self.ifc_methods.MarkLaunched(app_name)
            return True
        except Exception as e:
            print("Unexpected Error: {}".format(e))
            return False

    def RequestRemoveFromDesktop(self, app_name):
        """
        launcher中右键从桌面移除
        """
        return self.ifc_methods.RequestRemoveFromDesktop(app_name)

    def RequestSendToDesktop(self, app_name):
        """
        发送到桌面
        """
        return self.ifc_methods.RequestSendToDesktop(app_name)

    def RequestUninstall(self, app_name):
        """
        右键卸载
        """
        try:
            self.ifc_methods.RequestUninstall(app_name)
            return True
        except Exception as e:
            print("Unexpected Error: {}".format(e))
            return False

    def Search(self, string_value):
        """
        launcher中搜索的功能，需要监听SearchDone信号
        """
        try:
            self.ifc_methods.Search(string_value)
            return True
        except Exception as e:
            print("Unexpected Error: {}".format(e))
            return False

    def GetUseProxy(self, app_name):
        """
        获取某应用是否使用了代理
        """
        return self.ifc_methods.GetUseProxy(app_name)

    def SetUseProxy(self, app_name, bool_value):
        """
        设置某应用是否使用代理
        """
        try:
            self.ifc_methods.SetUseProxy(app_name, bool_value)
            return True
        except Exception as e:
            print("Unexpected Error: {}".format(e))
            return False

    def GetDisableScaling(self, app_name):
        """
        获取某应用是否关闭了缩放
        返回值：bool类型
        """
        return self.ifc_methods.GetDisableScaling(app_name)

    def SetDisableScaling(self, app_name, bool_value):
        """
        设置某应用是否关闭缩放
        """
        try:
            self.ifc_methods.SetDisableScaling(app_name, bool_value)
            return True
        except Exception as e:
            print("Unexpected Error: {}".format(e))
            return False

    def getFullscreen(self):
        """
        launcher是否是全屏显示
        返回值：bool
        """
        return self.ifc_properties.Get(self.interface,
                                       "Fullscreen")

    def getDisplayMode(self):
        """
        <value value="0" nick="free"/>
        <value value="1" nick="category"/>
        """
        value = self.ifc_properties.Get(self.interface,
                                       "DisplayMode")

        if 0 == value:
            return "free"
        else:
            return "category"
