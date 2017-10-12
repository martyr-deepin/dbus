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

        cls.screenshot_sc = '<Control><Alt>A'
        cls.new_screenshot_sc = '<Control><Alt>B'

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

    def testList(self):
        rt, shortcut_string = self.dbus_Keybinding.List()
        self.assertTrue(rt)
        self.assertTrue(shortcut_string != None)

    def testListContent(self):
        rt, shortcut_string = self.dbus_Keybinding.List()
        shortcut_list = json.loads(shortcut_string)

        systemIdList = []

        for i in self.systemFilter:
            for sc_item in  shortcut_list:
                if sc_item[self.shortcut_Type] != self.MEDIAKEY and sc_item[self.shortcut_Id] == i:
                    systemIdList.append(sc_item[self.shortcut_Id])
                    self.assertTrue(len(sc_item[self.shortcut_Accels]) > 0)
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

    def testCheckAvaliable(self):
        rt, string_accel = self.dbus_Keybinding.CheckAvaliable(self.new_screenshot_sc)
        self.assertTrue(rt)
        self.assertTrue('' == string_accel)

        rt, string_accel = self.dbus_Keybinding.CheckAvaliable(self.screenshot_sc)
        self.assertFalse(rt)
        self.assertFalse('' == string_accel)

    def testModifyShortcut(self):
        pass


def suite():
    suite = unittest.TestSuite()
    suite.addTest(Keybingding('testNumLockState'))
    suite.addTest(Keybingding('testModifyNumLockState'))
    suite.addTest(Keybingding('testList'))
    suite.addTest(Keybingding('testListContent'))
    suite.addTest(Keybingding('testCheckAvaliable'))
    return suite

if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')
