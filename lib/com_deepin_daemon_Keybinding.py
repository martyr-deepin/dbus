#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import os
import dbus

class DbusKeybinding:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Keybinding"
        self.obj_path = "/com/deepin/daemon/Keybinding"
        self.interface = "com.deepin.daemon.Keybinding"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,

                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)

        self.NumLockState = "NumLockState"

    def getNumLockState(self):
        return self.ifc_properties.Get(self.interface,
                                       self.NumLockState)
    def SetNumLockState(self, int_value):
        """
        int_value:
            0 关闭数字键盘
            1 开启数字键盘
        """
        try:
            self.ifc_methods.SetNumLockState(int_value)
            return True
        except:
            return False

    def List(self):
        """
        返回值：
            类型：string
            结构：json
            [{"Id":"move-to-workspace-11","Type":3,"Accels":[],"Name":"Move to workspace 11"},
            {"Id":"cycle-group","Type":3,"Accels":[],"Name":"Switch windows of an app directly"}]
        """
        try:
            return True, self.ifc_methods.List()
        except:
            return False, None

