#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import dbus
import unittest
import multiprocessing
from lib import DbusDaemonDock
from signals import WaitSignalMonitorDaemonDock

def mornitor():
    wait = WaitSignalMonitorDaemonDock()
    wait.run()

class DaemonDock(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dbus_DaemonDock = DbusDaemonDock()
        if os.path.exists('signal.txt'):
            os.remove('signal.txt')

    @classmethod
    def tearDownClass(cls):
        imageviewerDesktopFile = '/usr/share/applications/deepin-image-viewer.desktop'

        rt = cls.dbus_DaemonDock.IsDocked(imageviewerDesktopFile)
        if True == rt:
            cls.dbus_DaemonDock.RequestUndock(imageviewerDesktopFile)

    def testGetEntryIDs(self):
        id_list = self.dbus_DaemonDock.GetEntryIDs()
        self.assertTrue(len(id_list) > 0)

    def testMoveEntry(self):
        id_list = self.dbus_DaemonDock.GetEntryIDs()
        self.dbus_DaemonDock.MoveEntry(0, 1)
        id_list_new = self.dbus_DaemonDock.GetEntryIDs()
        self.assertTrue(id_list[0] == id_list_new[1])
        self.assertTrue(id_list[1] == id_list_new[0])
        self.dbus_DaemonDock.MoveEntry(0, 1)
        id_list_last = self.dbus_DaemonDock.GetEntryIDs()
        self.assertTrue(id_list_last == id_list)

    def testRequestDock(self):
        terminalDesktopFile = '/usr/share/applications/deepin-terminal.desktop'

        rt = self.dbus_DaemonDock.IsDocked(terminalDesktopFile)
        self.assertFalse(rt)

        rt = self.dbus_DaemonDock.RequestDock(terminalDesktopFile, 0)
        self.assertTrue(rt)
        rt = self.dbus_DaemonDock.IsDocked(terminalDesktopFile)
        self.assertTrue(rt)

        rt = self.dbus_DaemonDock.RequestUndock(terminalDesktopFile)
        self.assertTrue(rt)
        rt = self.dbus_DaemonDock.IsDocked(terminalDesktopFile)
        self.assertFalse(rt)

    def testRequestDockNumber(self):
        imageviewerDesktopFile = '/usr/share/applications/deepin-image-viewer.desktop'

        rt = self.dbus_DaemonDock.IsDocked(imageviewerDesktopFile)
        self.assertFalse(rt)

        w = multiprocessing.Process(target = mornitor)
        w.start()
        time.sleep(2)
        rt = self.dbus_DaemonDock.RequestDock(imageviewerDesktopFile, 0)
        self.assertTrue(rt)
        time.sleep(2)
        f = open('signal.txt', 'r')
        content = f.readline()
        f.close()
        position = int(content.split('|')[-1])
        self.assertTrue(0 == position, "%d" % position)
        rt = self.dbus_DaemonDock.IsDocked(imageviewerDesktopFile)
        id_list = self.dbus_DaemonDock.GetEntryIDs()
        self.assertTrue(rt)
        self.assertTrue(id_list[0] == 'deepin-image-viewer')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(DaemonDock('testGetEntryIDs'))
    suite.addTest(DaemonDock('testMoveEntry'))
    suite.addTest(DaemonDock('testRequestDock'))
    suite.addTest(DaemonDock('testRequestDockNumber'))

    return suite

if __name__ == "__main__":
    unittest.main(defaultTest = 'suite')
