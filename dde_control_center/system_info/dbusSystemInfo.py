#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbus

class DbusSystemInfo:
    def __init__(self):
        self.dbus_name = 'com.deepin.daemon.SystemInfo'
        self.dbus_path = '/com/deepin/daemon/SystemInfo'
        self.dbus_ifc  = 'com.deepin.daemon.SystemInfo'

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.dbus_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods = dbus.Interface(self.session_obj,
                dbus_interface=self.dbus_ifc)

    def getSystemType(self):
        return self.ifc_properties.Get(self.dbus_ifc, 'SystemType')

    def getDistroDesc(self):
        return self.ifc_properties.Get(self.dbus_ifc, 'DistroDesc')

    def getDistroID(self):
        return self.ifc_properties.Get(self.dbus_ifc, 'DistroID')

    def getDistroVer(self):
        return self.ifc_properties.Get(self.dbus_ifc, 'DistroVer')

    def getProcessor(self):
        return self.ifc_properties.Get(self.dbus_ifc, 'Processor')

    def getVersion(self):
        return self.ifc_properties.Get(self.dbus_ifc, 'Version')

    def getDiskCap(self):
        return self.ifc_properties.Get(self.dbus_ifc, 'DiskCap')

    def getMemoryCap(self):
        return self.ifc_properties.Get(self.dbus_ifc, 'MemoryCap')

