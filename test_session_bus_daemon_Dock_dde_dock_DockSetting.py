#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import dbus

def setUpModule():
    pass

def tearDownModule():
    pass

class testddedockDockSetting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.session_bus = dbus.SessionBus()
        cls.session_obj = cls.session_bus.get_object('com.deepin.daemon.Dock', '/dde/dock/DockSetting')
        cls.session_iface = dbus.Interface(cls.session_obj, dbus_interface='dde.dock.DockSetting')
        cls.default_DisplayMode = cls.session_iface.GetDisplayMode()
        cls.default_HideMode = cls.session_iface.GetHideMode()

    @classmethod
    def tearDownClass(cls):
        cls.session_iface.SetHideMode(cls.default_HideMode)
        cls.session_iface.SetDisplayMode(cls.default_DisplayMode)

    def setUp(self):
        pass

    def tearDown(self):
        self.session_iface.SetDisplayMode(self.default_DisplayMode)
        self.session_iface.SetHideMode(self.default_HideMode)

    def testddedockDockSettingHideMode(self):
        hidenum = self.session_iface.GetHideMode()
        self.assertEqual(hidenum, self.default_HideMode)
        tf_result = self.session_iface.SetHideMode(1)
        self.assertTrue(tf_result)
        self.assertEqual(self.session_iface.GetHideMode(), 1)
        tf_result = self.session_iface.SetHideMode(3)
        self.assertTrue(tf_result)
        self.assertEqual(self.session_iface.GetHideMode(), 3)
        tf_result = self.session_iface.SetHideMode(0)
        self.assertTrue(tf_result)
        self.assertEqual(self.session_iface.GetHideMode(), 0)

    def testddedockDockSettingHideModeFalse_one(self):
        tf_result = self.session_iface.SetHideMode(-1)
        self.assertFalse(tf_result)
        self.assertEqual(self.session_iface.GetHideMode(), self.default_HideMode)

    def testddedockDockSettingHideModeFalse_two(self):
        tf_result = self.session_iface.SetHideMode(4)
        self.assertFalse(tf_result)
        self.assertEqual(self.session_iface.GetHideMode(), self.default_HideMode)

    def testddedockDockSettingHideModeFalse_three(self):
        tf_result = self.session_iface.SetHideMode(2)
        self.assertFalse(tf_result)
        self.assertEqual(self.session_iface.GetHideMode(), self.default_HideMode)

    def testddedockDockSettingDisplayMode(self):
        tf_result = self.session_iface.SetDisplayMode(1)
        self.assertTrue(tf_result)
        self.assertEqual(self.session_iface.GetDisplayMode(), 1)
        tf_result = self.session_iface.SetDisplayMode(2)
        self.assertTrue(tf_result)
        self.assertEqual(self.session_iface.GetDisplayMode(), 2)
        tf_result = self.session_iface.SetDisplayMode(0)
        self.assertTrue(tf_result)
        self.assertEqual(self.session_iface.GetDisplayMode(), 0)

    def testddedockDockSettingDisplayModeFalse_one(self):
        tf_result = self.session_iface.SetDisplayMode(-1)
        self.assertFalse(tf_result)
        self.assertEqual(self.session_iface.GetDisplayMode(), self.default_DisplayMode)

    def testddedockDockSettingDisplayModeFalse_two(self):
        tf_result = self.session_iface.SetDisplayMode(3)
        self.assertFalse(tf_result)
        self.assertEqual(self.session_iface.GetDisplayMode(), self.default_DisplayMode)

def suite():
    suite = unittest.TestSuite()
    suite.addTest(testddedockDockSetting('testddedockDockSettingHideMode'))
    suite.addTest(testddedockDockSetting('testddedockDockSettingHideModeFalse_one'))
    suite.addTest(testddedockDockSetting('testddedockDockSettingHideModeFalse_two'))
    suite.addTest(testddedockDockSetting('testddedockDockSettingHideModeFalse_three'))
    suite.addTest(testddedockDockSetting('testddedockDockSettingDisplayMode'))
    suite.addTest(testddedockDockSetting('testddedockDockSettingDisplayModeFalse_one'))
    suite.addTest(testddedockDockSetting('testddedockDockSettingDisplayModeFalse_two'))
    return suite


if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')
