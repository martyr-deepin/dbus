#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import dbus
import unittest
from lib import DbusAccounts, DbusUser, DbusImageBlur
from lib import DbusSessionManager

class DaemonAccounts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.dbus_accounts = DbusAccounts()
        cls.dbus_session_manager = DbusSessionManager()
        cls.uid = cls.dbus_session_manager.getCurrentUid()

    @classmethod
    def tearDownClass(cls):
        pass

    def testFindUserById(self):
        object_path_by_uid = self.dbus_accounts.FindUserById(self.uid)
        dbus_user_object_path = self.dbus_accounts.FindUserById(self.uid)
        dbus_user = DbusUser(dbus_user_object_path)
        user_name = dbus_user.getUserName()
        user_uid  = dbus_user.getUid()
        object_path_by_name = self.dbus_accounts.FindUserByName(user_name)
        self.assertTrue(object_path_by_uid == object_path_by_name)
        self.assertTrue(self.uid == user_uid)

    def suite():
        suite = unittest.TestSuite()
        suite.addTest(DaemonAccounts('testFindUserById'))

        return suite

if __name__ == "__main__":
    unittest.TextTestRunner().run(DaemonAccounts.suite())
