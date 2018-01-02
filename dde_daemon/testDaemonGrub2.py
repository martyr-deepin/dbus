#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import dbus
import unittest
from lib import DbusGrub2

class DaemonGrub2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dbus_grub2 = DbusGrub2()

    @classmethod
    def tearDownClass(cls):
        pass

    def testGetSimpleEntryTitles(self):
        entry = self.dbus_grub2.GetSimpleEntryTitles()
        self.assertTrue(len(entry) > 0)

    def testgetEnableTheme(self):
        theme_status = self.dbus_grub2.getEnableTheme()
        self.assertTrue(theme_status == True or theme_status == False)

    def testgetTimeout(self):
        timeout = self.dbus_grub2.getTimeout()
        self.assertTrue(timeout == 5 or timeout == 1)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DaemonGrub2('testGetSimpleEntryTitles'))
        suite.addTest(DaemonGrub2('testgetEnableTheme'))
        suite.addTest(DaemonGrub2('testgetTimeout'))

        return suite

if __name__ == "__main__":
    unittest.TextTestRunner().run(DaemonGrub2.suite())
