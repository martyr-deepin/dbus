#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import dbus

class DbusAudio:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Audio"
        self.dbus_path  = "/com/deepin/daemon/Audio"
        self.dbus_ifc = "com.deepin.daemon.Audio"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.dbus_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.dbus_ifc)

    def getMaxUIVolume(self):
        """
        获取音频输入的最大值
        """
        return self.ifc_properties.Get(self.dbus_ifc,
                "MaxUIVolume")

    def getDefaultSink(self):
        """
        获取默认音频输出object path
        """
        return self.ifc_properties.Get(self.dbus_ifc,
                "DefaultSink")

    def getDefaultSource(self):
        """
        获取默认音频输入object path
        """
        return self.ifc_properties.Get(self.dbus_ifc,
                "DefaultSource")

    def SetDefaultSink(self, sink_obj_path):
        """
        设置默认输出
        """
        self.ifc_methods.SetDefaultSink(sink_obj_path)

    def SetDefaultSource(self, source_obj_path):
        """
        设置默认输入
        """
        self.ifc_methods.SetDefaultSource(source_obj_path)
