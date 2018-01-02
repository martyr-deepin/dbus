#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import dbus
import unittest
from lib import DbusGrub2, DbusTheme

class DaemonTheme(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dbus_grub2 = DbusGrub2()
        cls.dbus_theme = DbusTheme()

    @classmethod
    def tearDownClass(cls):
        pass

    def testGetBackground(self):
        background = self.dbus_theme.GetBackground()
        self.assertTrue(len(background) > 0)
        self.assertTrue(os.path.exists(background))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DaemonTheme('testGetBackground'))

        return suite

if __name__ == "__main__":
    unittest.TextTestRunner().run(DaemonTheme.suite())
