#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import dbus
import time
import unittest
from lib import DbusDisplay, DbusDisplayMonitorVGA, DbusDaemonDock

class Display(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dbus_dameondock = DbusDaemonDock()
        cls.dbus_display = DbusDisplay()
        cls.primary = cls.dbus_display.getPrimary()
        cls.dbus_primary_monitor = DbusDisplayMonitorVGA('/com/deepin/daemon/Display/Monitor' +
                                                         cls.primary)
        cls.rotation_dict = {0:1, 90:2, 180:4, 270:8}

    @classmethod
    def tearDownClass(cls):
        pass

    def testRotation(self):
        rotation = self.dbus_primary_monitor.getRotation()
        self.assertTrue(rotation == self.rotation_dict[0])
        screen_h = self.dbus_primary_monitor.getHeight()
        screen_w = self.dbus_primary_monitor.getWidth()
        rect0 = self.dbus_dameondock.getFrontendWindowRect()
        self.assertTrue(rect0[0] > 0)
        self.assertTrue(rect0[1] + rect0[3] == screen_h)

        rotation = self.dbus_primary_monitor.SetRotation(self.rotation_dict[90])
        self.dbus_display.ApplyChanges()
        time.sleep(5)
        rect90 = self.dbus_dameondock.getFrontendWindowRect()
        self.assertTrue(rect90[0] > 0)
        self.assertTrue(rect90[1] + rect90[3] == screen_w)
        rotation = self.dbus_primary_monitor.getRotation()
        self.assertTrue(rotation == self.rotation_dict[90])

        rotation = self.dbus_primary_monitor.SetRotation(self.rotation_dict[180])
        self.dbus_display.ApplyChanges()
        time.sleep(5)
        rect180 = self.dbus_dameondock.getFrontendWindowRect()
        self.assertTrue(rect180[0] > 0)
        self.assertTrue(rect180[1] + rect90[3] == screen_h)
        rotation = self.dbus_primary_monitor.getRotation()
        self.assertTrue(rotation == self.rotation_dict[180])

        rotation = self.dbus_primary_monitor.SetRotation(self.rotation_dict[270])
        self.dbus_display.ApplyChanges()
        time.sleep(5)
        rect270 = self.dbus_dameondock.getFrontendWindowRect()
        self.assertTrue(rect270[0] > 0)
        self.assertTrue(rect270[1] + rect270[3] == screen_w)
        rotation = self.dbus_primary_monitor.getRotation()
        self.assertTrue(rotation == self.rotation_dict[270])

        rotation = self.dbus_primary_monitor.SetRotation(self.rotation_dict[0])
        self.dbus_display.ApplyChanges()
        time.sleep(5)
        rect = self.dbus_dameondock.getFrontendWindowRect()
        self.assertTrue(rect[0] > 0)
        self.assertTrue(rect[1] + rect[3] == screen_h)
        rotation = self.dbus_primary_monitor.getRotation()
        self.assertTrue(rotation == self.rotation_dict[0])

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(Display('testRotation'))
        return suite

if __name__ == "__main__":
    unittest.TextTestRunner().run(Display.suite())
