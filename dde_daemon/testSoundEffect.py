#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import dbus
import time
import unittest
from lib import DbusSoundEffect

class SoundEffect(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dbus_soundeffect = DbusSoundEffect()

    @classmethod
    def tearDownClass(cls):
        pass

    def testPlaySystemSound(self):
        errorList = []
        for event_type in self.dbus_soundeffect.EventList:
            rt = self.dbus_soundeffect.PlaySystemSound(event_type)
            if rt == False:
                errorList.append(event_type)

        self.assertTrue(len(errorList) == 0, "errorList : %s" % str(errorList))

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(SoundEffect('testPlaySystemSound'))
        return suite

if __name__ == "__main__":
    unittest.TextTestRunner().run(SoundEffect.suite())
