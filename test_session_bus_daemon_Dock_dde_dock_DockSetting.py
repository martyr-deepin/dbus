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
        cls.default_ClockType = cls.session_iface.GetClockType()
        cls.default_DisplayDate = cls.session_iface.GetDisplayDate()
        cls.default_DisplayMode = cls.session_iface.GetDisplayMode()
        cls.default_DisplayWeek = cls.session_iface.GetDisplayWeek()
        cls.default_HideMode = cls.session_iface.GetHideMode()

    @classmethod
    def tearDownClass(cls):
        cls.session_iface.SetHideMode(cls.default_HideMode)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testddedockDockSettingHideMode(self):
        hidenum = self.session_iface.GetHideMode()
        self.assertEqual(hidenum, self.default_HideMode)
        tf_result = self.session_iface.SetHideMode(1)
        self.assertTrue(tf_result)
        self.assertEqual(self.session_iface.GetHideMode(), 1)
        tf_result = self.session_iface.SetHideMode(2)
        self.assertTrue(tf_result)
        self.assertEqual(self.session_iface.GetHideMode(), 2)
        tf_result = self.session_iface.SetHideMode(3)
        self.assertTrue(tf_result)
        self.assertEqual(self.session_iface.GetHideMode(), 3)
        tf_result = self.session_iface.SetHideMode(0)
        self.assertTrue(tf_result)
        self.assertEqual(self.session_iface.GetHideMode(), 0)

    def testddedockDockSettingHideModeFalse(self):
        hidenum = self.session_iface.GetHideMode()
        tf_result = self.session_iface.SetHideMode(-1)
        self.assertFalse(tf_result)
        self.assertEqual(self.session_iface.GetHideMode(), hidenum)
        tf_result = self.session_iface.SetHideMode(4)
        self.assertFalse(tf_result)
        self.assertEqual(self.session_iface.GetHideMode(), hidenum)
        tf_result = self.session_iface.SetHideMode(4000)
        self.assertFalse(tf_result)
        self.assertEqual(self.session_iface.GetHideMode(), hidenum)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(testddedockDockSetting('testddedockDockSettingHideMode'))
    suite.addTest(testddedockDockSetting('testddedockDockSettingHideModeFalse'))
    return suite


if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')
