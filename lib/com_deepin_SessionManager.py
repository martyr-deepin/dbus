#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import dbus

class SessionManager:
    def __init__(self):
        self.dbus_name = "com.deepin.SessionManager"
        self.obj_path  = "/com/deepin/SessionManager"
        self.interface = "com.deepin.SessionManager"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)

        self.dbus_properties_Stage = "Stage"
        self.dbus_properties_CurrentUid = "CurrentUid"

    def CanHibernate(self):
        return self.ifc_methods.CanHibernate()

    def CanLogout(self):
        return self.ifc_methods.CanLogout()

    def CanReboot(self):
        return self.ifc_methods.CanReboot()

    def CanShutdown(self):
        return self.ifc_methods.CanShutdown()

    def CanSuspend(self):
        return self.ifc_methods.CanSuspend()

    def getStage(self):
        return self.ifc_properties.Get(self.interface,
                self.dbus_properties_Stage)

    def getCurrentUid(self):
        return self.ifc_properties.Get(self.interface,
                self.dbus_properties_CurrentUid)

    def RequestLogout(self):
        self.ifc_methods.RequestLogout()