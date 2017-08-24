#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import os
import dbus

class Accounts:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Accounts"
        self.obj_path  = "/com/deepin/daemon/Accounts"
        self.interface = "com.deepin.daemon.Accounts"

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.system_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.system_obj,
                dbus_interface=self.interface)

    def FindUserById(self, Id):
        return self.ifc_methods.FindUserById(Id)

    def RandUserIcon(self):
        return self.ifc_methods.RandUserIcon()


class User:
    def __init__(self, UserObjPath):
        self.dbus_name = "com.deepin.daemon.Accounts"
        self.obj_path  = UserObjPath
        self.interface = "com.deepin.daemon.Accounts.User"

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.system_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.system_obj,
                dbus_interface=self.interface)

        self.dbus_properties_IconFile = "IconFile"
        self.dbus_properties_Uid = "Uid"
        self.dbus_properties_UserName = "UserName"

    def getIconFile(self):
        return self.ifc_properties.Get(self.interface,
                self.dbus_properties_IconFile)

    def getUid(self):
        return self.ifc_properties.Get(self.interface,
                self.dbus_properties_Uid)

    def getUserName(self):
        return self.ifc_properties.Get(self.interface,
                self.dbus_properties_UserName)

    def SetPassword(self, pw):
        pid = os.fork()

        if 0 == pid:
            self.ifc_methods.SetPassword(pw)
