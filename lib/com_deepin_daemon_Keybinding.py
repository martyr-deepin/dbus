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

    def CheckAvaliable(self, string_accel):
        """
        检查快捷键是否可用：
            返回值：(Boolean arg_1, String arg_2)
            arg_1: True or False，是否可用
            arg_2: 与之冲突的快捷键详细信息，是JSON字符串，如果没有冲突，则为空字符串

            例子：
            False, '{"Id":"screenshot","Type":0,"Accels":["\\u003cControl\\u003e\\u003cAlt\\u003eA"],"Name":"Screenshot"}'

        参考：
        signal KeyEvent(Boolean, String): 快捷键是否被按下，快捷键字符串accel
        例如：accel值
                <Control><Alt>A
                <Control><Alt>a

                control, alt, super, shift不区分大小写，Keybinding会转换成小写字母处理
        """
        return self.ifc_methods.CheckAvaliable(string_accel)

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

