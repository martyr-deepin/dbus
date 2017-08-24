#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbus

class DbusNetworkManager:
    def __init__(self):
        self.dbus_name = 'org.freedesktop.NetworkManager'
        self.dbus_path = '/org/freedesktop/NetworkManager'
        self.dbus_ifc  = 'org.freedesktop.NetworkManager'

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_name,
                self.dbus_path)
        self.ifc_properties = dbus.Interface(self.system_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods = dbus.Interface(self.system_obj,
                dbus_interface=self.dbus_ifc)

    def getPrimaryConnection(self):
        return self.ifc_properties.Get(self.dbus_ifc,
                "PrimaryConnection")

    def getPrimaryConnectionType(self):
        return self.ifc_properties.Get(self.dbus_ifc,
                "PrimaryConnectionType")

    def GetAllDevices(self):
        return self.ifc_methods.GetAllDevices()

class DbusNetworkManagerSettings:
    def __init__(self):
        self.dbus_name = 'org.freedesktop.NetworkManager'
        self.dbus_path = '/org/freedesktop/NetworkManager/Settings'
        self.dbus_ifc  = 'org.freedesktop.NetworkManager.Settings'

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_name,
                self.dbus_path)
        self.ifc_properties = dbus.Interface(self.system_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods = dbus.Interface(self.system_obj,
                dbus_interface=self.dbus_ifc)

    def getConnections(self):
        return self.ifc_properties.Get(self.dbus_ifc,
                "Connections")

class DbusNetworkManagerActiveConnection(object_path):
    def __init__(self):
        self.dbus_name = 'org.freedesktop.NetworkManager'
        self.dbus_path = object_path
        self.dbus_ifc  = 'org.freedesktop.NetworkManager.Connection.Active'

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_name,
                self.dbus_path)
        self.ifc_properties = dbus.Interface(self.system_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods = dbus.Interface(self.system_obj,
                dbus_interface=self.dbus_ifc)

    def getDhcp4Config(self):
        return self.ifc_properties.Get(self.dbus_ifc,
                "Dhcp4Config")

class DbusNetworkManagerDHCP4Config(object_path):
    def __init__(self):
        self.dbus_name = 'org.freedesktop.NetworkManager'
        self.dbus_path = object_path
        self.dbus_ifc  = 'org.freedesktop.NetworkManager.DHCP4Config'

        self.system_bus = dbus.SystemBus()
        self.system_obj = self.system_bus.get_object(self.dbus_name,
                self.dbus_path)
        self.ifc_properties = dbus.Interface(self.system_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods = dbus.Interface(self.system_obj,
                dbus_interface=self.dbus_ifc)

    def getOption(self):
        return self.ifc_properties.Get(self.dbus_ifc,
                "Option")

