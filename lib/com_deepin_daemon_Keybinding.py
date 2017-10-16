#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import os
import dbus
import json

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

    def LookupConflictingShortcut(self, string_accel):
        """
        检查快捷键是否可用：
            返回值：(Boolean arg_1, String arg_2)
            arg_1: True or False，是否可用
            arg_2: 与之冲突的快捷键详细信息，是JSON字符串，如果没有冲突，则为空字符串

            例子：
            '{"Id":"screenshot","Type":0,"Accels":["\\u003cControl\\u003e\\u003cAlt\\u003eA"],"Name":"Screenshot"}'

        参考：
        signal KeyEvent(Boolean, String): 快捷键是否被按下，快捷键字符串accel
        例如：accel值
                <Control><Alt>A
                <Control><Alt>a

                control, alt, super, shift不区分大小写，Keybinding会转换成小写字母处理
        """
        return True, self.ifc_methods.LookupConflictingShortcut(string_accel)

    def ListAllShortcuts(self):
        """
        返回值：
            类型：string
            结构：json
            [{"Id":"move-to-workspace-11","Type":3,"Accels":[],"Name":"Move to workspace 11"},
            {"Id":"cycle-group","Type":3,"Accels":[],"Name":"Switch windows of an app directly"}]
        """
        try:
            return True, self.ifc_methods.ListAllShortcuts()
        except:
            return False, None

    def AddShortcutKeystroke(self, string_id, int_type, string_keystroke):
        """
        添加快捷键设置：
            string_id:  screenshot
            int_type:   0
            string_keystroke:   <Control><Alt>A

        返回值:
            无
        """
        try:
            self.ifc_methods.AddShortcutKeystroke(string_id, int_type, string_keystroke)
            return True
        except:
            return False

    def DeleteShortcutKeystroke(self, string_id, int_type, string_keystroke):
        """
        删除快捷键：
            string_id:  screenshot
            int_type:   0
            string_keystroke:   <Control><Alt>A

        返回值：
            无
        """
        try:
            self.ifc_methods.DeleteShortcutKeystroke(string_id, int_type, string_keystroke)
            return True
        except:
            return False

    def GetShortcut(self, string_id, string_type):
        """
        获取快捷键信息：
        入参：
            string_id:  快捷键Id值
            string_type: 快捷键type值

        返回值：
            json字符串:
                {"Id":"screenshot","Type":0,"Accels":["\u003cControl\u003e\u003cAlt\u003eA"],"Name":"截图"}
            请参考文档keydetail.txt
        """
        return json.loads(self.ifc_methods.GetShortcut(string_id, string_type))

    def ClearShortcutKeystrokes(self, string_id, string_type):
        """
        删除所有快捷键：
            string_id:      快捷键Id值
            string_type:    快捷键type值

        返回值：
            无
        """
        try:
            self.ifc_methods.ClearShortcutKeystrokes(string_id, string_type)
            return True
        except:
            return False
