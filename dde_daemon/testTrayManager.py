#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import dbus
import unittest
from lib import DbusTrayManager

class Icon:
    def __init__(self, wid, name):
        self.wid = wid
        self.name = name

class TrayManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dbus_TrayManager = DbusTrayManager()

    @classmethod
    def tearDownClass(cls):
        pass

    def testGetName(self):
        trayicons = self.dbus_TrayManager.getTrayIcons()
        icons = []
        for wid in trayicons:
            name = self.dbus_TrayManager.GetName(wid)
            icon = Icon(wid, name)
            icons.append(icon)

        self.assertTrue(len(trayicons) > 0)

        sogouqimpanel_exist = False

        for icon in icons:
            if "sogou-qimpanel" == icon.name:
                sogouqimpanel_exist = True
            self.assertTrue(icon.wid > 0)
            self.assertTrue(len(icon.name) > 0)

        self.assertTrue(sogouqimpanel_exist)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(TrayManager('testGetName'))

        return suite

if __name__ == "__main__":
    unittest.TextTestRunner().run(TrayManager.suite())
