#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import dbus
import unittest
from lib import DbusSystemInfo
from lib import DbusUDisks2
from subprocess import getoutput

versionFileDeepin = "/etc/deepin-version"
versionFileLSB    = "/etc/lsb-release"

versionGroupRelease = "Release"
versionKeyVersion   = "Version"
versionKeyType      = "Type"

versionKeyLSB   = "DISTRIB_RELEASE"
versionKeyDelim = "="

distroIdKeyLSB   = "DISTRIB_ID"
distroDescKeyLSB = "DISTRIB_DESCRIPTION"
distroVerKeyLSB  = "DISTRIB_RELEASE"
distroKeyDelim   = "="

class SystemInfo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dbus_systeminfo = DbusSystemInfo()
        cls.dbus_udisk2 = DbusUDisks2()

    @classmethod
    def tearDownClass(cls):
        pass

    def testVersionFileExist(self):
        self.assertTrue(os.path.exists(versionFileDeepin))
        self.assertTrue(os.path.exists(versionFileLSB))

    def testPropertiesSystemType(self):
        command_value = int(getoutput("/usr/bin/getconf LONG_BIT"))
        dbus_value = self.dbus_systeminfo.getSystemType()
        self.assertTrue(command_value == dbus_value)

    def testPropertiesDistroDesc(self):
        d = parseInfoFile(versionFileLSB, versionKeyDelim)
        dbus_DistroDesc = self.dbus_systeminfo.getDistroDesc()
        self.assertTrue(d[distroDescKeyLSB][1:-1] == dbus_DistroDesc, d)

    def testPropertiesDistroID(self):
        d = parseInfoFile(versionFileLSB, versionKeyDelim)
        dbus_DistroID = self.dbus_systeminfo.getDistroID()
        self.assertTrue(d[distroIdKeyLSB] == dbus_DistroID)

    def testPropertiesDistroVer(self):
        d = parseInfoFile(versionFileLSB, versionKeyDelim)
        dbus_DistroVer = self.dbus_systeminfo.getDistroVer()
        self.assertTrue(d[distroVerKeyLSB] == dbus_DistroVer)

    def testPropertiesDiskCap(self):
        udisk_value = self.dbus_udisk2.GetManagedObjects()

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(SystemInfo('testVersionFileExist'))
        suite.addTest(SystemInfo('testPropertiesSystemType'))
        suite.addTest(SystemInfo('testPropertiesDistroDesc'))
        suite.addTest(SystemInfo('testPropertiesDistroID'))
        suite.addTest(SystemInfo('testPropertiesDistroVer'))
        suite.addTest(SystemInfo('testPropertiesDiskCap'))
        return suite

def getVersionFromDeepin(filePath):
    pass

def getVersionFromLSB(filePath):
    pass

def parseInfoFile(filePath, delim):
    f = open(filePath, 'r')
    ret = {}

    for line in f.readlines():
        line = line.strip()
        key, value = line.split(delim)
        ret[key] = value

    f.close()

    return ret

if __name__ == "__main__":
    unittest.TextTestRunner().run(SystemInfo.suite())
