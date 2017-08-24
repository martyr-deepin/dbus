#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import dbus

class LangSelector:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.LangSelector"
        self.obj_path  = "/com/deepin/daemon/LangSelector"
        self.interface = "com.deepin.daemon.LangSelector"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)

    def GetLocaleList(self):
        return self.ifc_methods.GetLocaleList()

    def SetLocale(self, langinfo):
        self.ifc_methods.SetLocale(langinfo)