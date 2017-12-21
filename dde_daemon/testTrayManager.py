#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import dbus
import unittest
import multiprocessing
from lib import DbusTrayManager
from lib import Utils
from signals import WaitSignalMonitorTrayManager

def monitor():
    wait = WaitSignalMonitorTrayManager()
    wait.run()

class Icon:
    def __init__(self, wid, name):
        self.wid = wid
        self.name = name

class TrayManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dbus_TrayManager = DbusTrayManager()
        Utils.clearCache()

    @classmethod
    def tearDownClass(cls):
        pass

    def testGetName(self):
        icons = self.getIcons()
        sogouqimpanel_exist = False

        for icon in icons:
            if "sogou-qimpanel" == icon.name:
                sogouqimpanel_exist = True
            self.assertTrue(icon.wid > 0)
            self.assertTrue(len(icon.name) > 0)

        self.assertTrue(sogouqimpanel_exist)

    def testSignalAdded(self):
        w = multiprocessing.Process(target = monitor)
        w.start()
        time.sleep(2)
        os.system("deepin-music > /dev/null &")
        time.sleep(10)
        content = Utils.readSignalFile()
        wid = int(content.split('|')[-1])
        event = content.split('|')[-2]
        self.assertTrue("深度音乐" == self.dbus_TrayManager.GetName(wid))
        self.assertTrue("Added" == event)

    def testSignalRemoved(self):
        icons = self.getIcons()
        for icon in icons:
            if "深度音乐" == icon.name:
                deepin_music_wid = icon.wid

        w = multiprocessing.Process(target = monitor)
        w.start()
        time.sleep(2)
        os.system("killall deepin-music")
        time.sleep(2)
        content = Utils.readSignalFile()
        wid = int(content.split('|')[-1])
        event = content.split('|')[-2]
        self.assertTrue(wid == deepin_music_wid)
        self.assertTrue("Removed" == event)

    def getIcons(self):
        trayicons = self.dbus_TrayManager.getTrayIcons()
        icons = []
        for wid in trayicons:
            name = self.dbus_TrayManager.GetName(wid)
            icon = Icon(wid, name)
            icons.append(icon)

        return icons

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(TrayManager('testGetName'))
        suite.addTest(TrayManager('testSignalAdded'))
        suite.addTest(TrayManager('testSignalRemoved'))

        return suite

if __name__ == "__main__":
    unittest.TextTestRunner().run(TrayManager.suite())
