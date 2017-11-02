#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import dbus
import json
import unittest
from lib import DbusKeybinding
from subprocess import getoutput

class Keybingding(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dbus_Keybinding = DbusKeybinding()
        cls.NumLockState = cls.dbus_Keybinding.getNumLockState()

        cls.MEDIAKEY = 2
        cls.CUSTOMKEY = 1

        cls.CUSTOM_ID_LENGTH = 32

        cls.shortcut_Id = "Id"
        cls.shortcut_Accels = "Accels"
        cls.shortcut_Name = "Name"
        cls.shortcut_Type = "Type"
        cls.shortcut_Exec = "Exec"

        cls.systemFilter = ["terminal",
                            "terminal-quake",
                            "screenshot",
                            "screenshot-delayed",
                            "screenshot-window",
                            "deepin-screen-recorder",
                            "switch-group",
                            "switch-group-backward",
                            "preview-workspace",
                            "expose-windows",
                            "expose-all-windows",
                            "launcher",
                            "switch-applications",
                            "switch-applications-backward",
                            "show-desktop",
                            "file-manager",
                            "lock-screen",
                            "logout",
                            "wm-switcher"]

        cls.windowFilter = ["maximize",
                            "unmaximize",
                            "minimize",
                            "begin-move",
                            "begin-resize",
                            "close"]

        cls.workspaceFilter = ["switch-to-workspace-left",
                               "switch-to-workspace-right",
                               "move-to-workspace-left",
                               "move-to-workspace-right"]

        cls.screenshot_Id = 'screenshot'
        cls.screenshot_Type = 0
        cls.screenshot_sc = '<Control><Alt>A'
        cls.new_screenshot_sc = '<Control><Alt>B'

        cls.custom_shortcut_id = ''

    @classmethod
    def tearDownClass(cls):
        cls.dbus_Keybinding.SetNumLockState(cls.NumLockState)

    def testNumLockState(self):
        self.assertIn(self.NumLockState, [0, 1])

    def testModifyNumLockState(self):
        rt = self.dbus_Keybinding.SetNumLockState(0)
        self.assertTrue(rt)

        rt = self.dbus_Keybinding.SetNumLockState(1)
        self.assertTrue(rt)

        rt = self.dbus_Keybinding.SetNumLockState(2)
        self.assertFalse(rt)

        rt = self.dbus_Keybinding.SetNumLockState(3)
        self.assertFalse(rt)

        rt = self.dbus_Keybinding.SetNumLockState(100)
        self.assertFalse(rt)

        rt = self.dbus_Keybinding.SetNumLockState(-1)
        self.assertFalse(rt)

        rt = self.dbus_Keybinding.SetNumLockState(-100)
        self.assertFalse(rt)

    def testListAllShortcuts(self):
        rt, shortcut_string = self.dbus_Keybinding.ListAllShortcuts()
        self.assertTrue(rt)
        self.assertTrue(shortcut_string != None)

    def testListContent(self):
        rt, shortcut_string = self.dbus_Keybinding.ListAllShortcuts()
        shortcut_list = json.loads(shortcut_string)

        systemIdList = []

        for i in self.systemFilter:
            for sc_item in  shortcut_list:
                if sc_item[self.shortcut_Type] != self.MEDIAKEY and sc_item[self.shortcut_Id] == i:
                    systemIdList.append(sc_item[self.shortcut_Id])
                    self.assertTrue(len(sc_item[self.shortcut_Accels]) > 0, "Id: %s accels: %s" %
                                    (sc_item[self.shortcut_Id], sc_item[self.shortcut_Accels]))
                    self.assertTrue(len(sc_item[self.shortcut_Name]) > 0)
                    break

        self.assertTrue(self.systemFilter == systemIdList)


        windowIdList = []

        for i in self.windowFilter:
            for sc_item in  shortcut_list:
                if sc_item[self.shortcut_Type] != self.MEDIAKEY and sc_item[self.shortcut_Id] == i:
                    windowIdList.append(sc_item[self.shortcut_Id])
                    self.assertTrue(len(sc_item[self.shortcut_Accels]) > 0)
                    self.assertTrue(len(sc_item[self.shortcut_Name]) > 0)
                    break

        self.assertTrue(self.windowFilter == windowIdList)

        workspaceIdList = []

        for i in self.workspaceFilter:
            for sc_item in  shortcut_list:
                if sc_item[self.shortcut_Type] != self.MEDIAKEY and sc_item[self.shortcut_Id] == i:
                    workspaceIdList.append(sc_item[self.shortcut_Id])
                    self.assertTrue(len(sc_item[self.shortcut_Accels]) > 0)
                    self.assertTrue(len(sc_item[self.shortcut_Name]) > 0)
                    break

        self.assertTrue(self.workspaceFilter == workspaceIdList)

        for sc_item in shortcut_list:
            if sc_item[self.shortcut_Type] != self.MEDIAKEY and \
               sc_item[self.shortcut_Type] == self.CUSTOMKEY:
                string_Id = sc_item[self.shortcut_Id].replace('-', '')
                self.assertEqual(len(string_Id), self.CUSTOM_ID_LENGTH)
                self.assertTrue(len(sc_item[self.shortcut_Accels]) > 0)
                self.assertTrue(len(sc_item[self.shortcut_Name]) > 0)
                self.assertTrue(len(sc_item[self.shortcut_Exec]) > 0)

    def testLookupConflictingShortcut(self):
        rt, string_accel = self.dbus_Keybinding.LookupConflictingShortcut(self.new_screenshot_sc)
        self.assertTrue(rt)
        self.assertTrue('' == string_accel)

        rt, string_accel = self.dbus_Keybinding.LookupConflictingShortcut(self.screenshot_sc)
        self.assertTrue(rt)
        self.assertFalse('' == string_accel, "string_accel: %s" % string_accel)

    def testModifyShortcut(self):
        info = self.dbus_Keybinding.GetShortcut(self.screenshot_Id, self.screenshot_Type)
        accel = info[self.shortcut_Accels]
        self.assertTrue(accel[0] == self.screenshot_sc, "accel: %s \
                        self.screenshot_sc: %s" %
                        (accel[0], self.screenshot_sc))

        rt = self.dbus_Keybinding.AddShortcutKeystroke(self.screenshot_Id, self.screenshot_Type,
                                                       self.new_screenshot_sc)
        self.assertTrue(rt)

        info = self.dbus_Keybinding.GetShortcut(self.screenshot_Id, self.screenshot_Type)
        accel = info[self.shortcut_Accels]
        self.assertIn(self.new_screenshot_sc, accel, "accel: %s \
                        self.new_screenshot_sc: %s" %
                        (accel, self.new_screenshot_sc))
        self.assertIn(self.screenshot_sc, accel, "accel: %s \
                        self.screenshot_sc: %s" %
                        (accel, self.screenshot_sc))

        rt = self.dbus_Keybinding.DeleteShortcutKeystroke(self.screenshot_Id, self.screenshot_Type,
                                                     self.new_screenshot_sc)
        self.assertTrue(rt)
        info = self.dbus_Keybinding.GetShortcut(self.screenshot_Id, self.screenshot_Type)
        accel = info[self.shortcut_Accels]
        self.assertTrue(len(accel) == 1, "accel: %s" % str(accel))
        self.assertTrue(self.new_screenshot_sc not in accel)
        self.assertTrue(self.screenshot_sc in accel)

    def testClearShortcutKeystrokes(self):
        info = self.dbus_Keybinding.GetShortcut(self.screenshot_Id, self.screenshot_Type)
        accel = info[self.shortcut_Accels]
        self.assertTrue(len(accel) == 1, "accel: %s" % str(accel))
        self.assertTrue(self.new_screenshot_sc not in accel)
        self.assertTrue(self.screenshot_sc in accel)

        rt = self.dbus_Keybinding.ClearShortcutKeystrokes(self.screenshot_Id, self.screenshot_Type)
        self.assertTrue(rt)
        info = self.dbus_Keybinding.GetShortcut(self.screenshot_Id, self.screenshot_Type)
        accel = info[self.shortcut_Accels]
        self.assertTrue(len(accel) == 0)
        self.assertTrue(self.new_screenshot_sc not in accel)
        self.assertTrue(self.screenshot_sc not in accel)

        rt = self.dbus_Keybinding.AddShortcutKeystroke(self.screenshot_Id, self.screenshot_Type,
                                                       self.screenshot_sc)
        self.assertTrue(rt)
        info = self.dbus_Keybinding.GetShortcut(self.screenshot_Id, self.screenshot_Type)
        accel = info[self.shortcut_Accels]
        self.assertTrue(len(accel) == 1)
        self.assertTrue(self.new_screenshot_sc not in accel)
        self.assertTrue(self.screenshot_sc in accel)

    def testAddCustomShortcut(self):
        custom_sc_list = self.getCustomShortcut()

        add_name = "自定义zidingyi"
        add_action = "/usr/bin/deepin-image-viewer"
        add_keystroke = "<Control><Alt>V"
        rt, (self.custom_shortcut_id, int_type) = self.dbus_Keybinding.AddCustomShortcut(add_name, add_action, add_keystroke)
        custom_shortcut_id = self.custom_shortcut_id
        self.assertTrue(rt)
        self.assertTrue(len(custom_shortcut_id.replace('-', '')) == self.CUSTOM_ID_LENGTH, "custom_shortcut_id:\
    %s" % str(self.custom_shortcut_id))

    def testModifyCustomShortcut(self):
        custom_sc_item = self.getCustomShortcutByName("自定义zidingyi")
        self.assertTrue(custom_sc_item != None)
        custom_sc_id = custom_sc_item[self.shortcut_Id]

        modify_name = "自定义zidingyi_modify"
        modify_action = "/usr/bin/deepin-terminal"
        modify_keystroke = "<Control><Alt>M"
        rt = self.dbus_Keybinding.ModifyCustomShortcut(custom_sc_id, modify_name, modify_action, modify_keystroke)
        self.assertTrue(rt)

        custom_sc_item = self.getCustomShortcutByName("自定义zidingyi_modify")
        self.assertTrue(custom_sc_item != None)
        self.assertTrue(custom_sc_item[self.shortcut_Id] == custom_sc_id)
        self.assertTrue(custom_sc_item[self.shortcut_Name] == modify_name)
        self.assertTrue(custom_sc_item[self.shortcut_Exec] == modify_action)
        self.assertTrue(custom_sc_item[self.shortcut_Accels][0] == modify_keystroke)

    def testDeleteCustomShortcut(self):
        custom_sc_item = self.getCustomShortcutByName("自定义zidingyi_modify")
        self.assertTrue(custom_sc_item != None)

        custom_sc_id = custom_sc_item[self.shortcut_Id]
        rt = self.dbus_Keybinding.DeleteCustomShortcut(custom_sc_id)
        self.assertTrue(rt)
        custom_sc_item = self.getCustomShortcutById(custom_sc_id)
        self.assertTrue(custom_sc_item == None)

    def getCustomShortcut(self):
        """
        查询自定义快捷键信息，返回类型为list
        """
        rt, shortcut_string = self.dbus_Keybinding.ListAllShortcuts()
        shortcut_list = json.loads(shortcut_string)

        customshortcut_list = []

        for sc_item in shortcut_list:
            if sc_item[self.shortcut_Type] != self.MEDIAKEY and \
               sc_item[self.shortcut_Type] == self.CUSTOMKEY:
                customshortcut_list.append(sc_item)

        return customshortcut_list

    def getCustomShortcutById(self, string_id):
        custom_sc_list = self.getCustomShortcut()

        for sc_item in  custom_sc_list:
            if sc_item[self.shortcut_Id] == string_id:
                return sc_item

        return None

    def getCustomShortcutByName(self, string_name):
        custom_sc_list = self.getCustomShortcut()

        for sc_item in  custom_sc_list:
            if sc_item[self.shortcut_Name] == string_name:
                return sc_item

        return None

def suite():
    suite = unittest.TestSuite()
    suite.addTest(Keybingding('testNumLockState'))
    suite.addTest(Keybingding('testModifyNumLockState'))
    suite.addTest(Keybingding('testListAllShortcuts'))
    suite.addTest(Keybingding('testListContent'))
    suite.addTest(Keybingding('testLookupConflictingShortcut'))
    suite.addTest(Keybingding('testModifyShortcut'))
    suite.addTest(Keybingding('testClearShortcutKeystrokes'))
    suite.addTest(Keybingding('testAddCustomShortcut'))
    suite.addTest(Keybingding('testModifyCustomShortcut'))
    suite.addTest(Keybingding('testDeleteCustomShortcut'))
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')
