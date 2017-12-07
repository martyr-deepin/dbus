#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import dbus
import unittest
import multiprocessing
from lib import DbusDaemonLauncher
from schema import SchemaLauncher
from signals import WaitSignalMonitorDaemonDock

class DaemonLauncher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dbus_DaemonLauncher = DbusDaemonLauncher()
        cls.schema_Launcher = SchemaLauncher()

    @classmethod
    def tearDownClass(cls):
        pass

    def testGetDisableScaling(self):
        is_scaling = self.dbus_DaemonLauncher.GetDisableScaling('deepin-terminal')
        self.assertTrue(False == is_scaling)

    def testSetDisableScaling(self):
        rt = self.dbus_DaemonLauncher.SetDisableScaling('deepin-terminal', True)
        self.assertTrue(True == rt)
        time.sleep(1)
        is_scaling = self.dbus_DaemonLauncher.GetDisableScaling('deepin-terminal')
        self.assertTrue(True == is_scaling)
        app_disable_list = self.schema_Launcher.getKeyDisableScaling()
        self.assertTrue('deepin-terminal' in app_disable_list)

        rt = self.dbus_DaemonLauncher.SetDisableScaling('deepin-terminal', False)
        self.assertTrue(True == rt)
        time.sleep(1)
        is_scaling = self.dbus_DaemonLauncher.GetDisableScaling('deepin-terminal')
        self.assertTrue(False == is_scaling)
        app_disable_list = self.schema_Launcher.getKeyDisableScaling()
        self.assertTrue('deepin-terminal' not in app_disable_list)

    def testSetDisableScalingInvalidAppName(self):
        rt = self.dbus_DaemonLauncher.SetDisableScaling('deepin-terminal-invalid', True)
        self.assertTrue(False == rt)
        time.sleep(1)
        try:
            is_scaling = self.dbus_DaemonLauncher.GetDisableScaling('deepin-terminal-invalid')
            self.assertTrue(False)
        except:
            self.assertTrue(True)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DaemonLauncher('testGetDisableScaling'))
        suite.addTest(DaemonLauncher('testSetDisableScaling'))
        suite.addTest(DaemonLauncher('testSetDisableScalingInvalidAppName'))

        return suite

if __name__ == "__main__":
    unittest.TextTestRunner().run(DaemonLauncher.suite())
