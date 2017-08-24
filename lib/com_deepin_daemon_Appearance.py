#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import dbus

class DbusAppearance:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.Appearance"
        self.obj_path  = "/com/deepin/daemon/Appearance"
        self.interface = "com.deepin.daemon.Appearance"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)

    def getFontSize(self):
        return self.ifc_properties.Get(self.interface,
                "FontSize")

    def getBackground(self):
        return self.ifc_properties.Get(self.interface,
                "Background")

    def getCursorTheme(self):
        return self.ifc_properties.Get(self.interface,
                "CursorTheme")

    def getGtkTheme(self):
        return self.ifc_properties.Get(self.interface,
                "GtkTheme")

    def getIconTheme(self):
        return self.ifc_properties.Get(self.interface,
                "IconTheme")

    def getMonospaceFont(self):
        return self.ifc_properties.Get(self.interface,
                "MonospaceFont")

    def getStandardFont(self):
        return self.ifc_properties.Get(self.interface,
                "StandardFont")

    def List(self, category):
        return self.ifc_methods.List(category)

    def Show(self, typename):
        return self.ifc_methods.Show(typename)

    def Thumbnail(self, typename, themename):
        return self.ifc_methods.Thumbnail(typename, themename)
