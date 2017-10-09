#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import os
import dbus

class DbusInputDevicesMouse:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.InputDevices"
        self.obj_path = "/com/deepin/daemon/InputDevices/Mouse"
        self.interface = "com.deepin.daemon.InputDevices.Mouse"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,

                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)

        self.LeftHanded = "LeftHanded"
        self.NaturalScroll = "NaturalScroll"
        self.MotionAcceleration = "MotionAcceleration"
        self.DoubleClick = "DoubleClick"

    def getLeftHanded(self):
        return self.ifc_properties.Get(self.interface,
                                       self.LeftHanded)

    def setLeftHanded(self, bool_value):
        self.ifc_properties.Set(self.interface, self.LeftHanded,
                                bool_value)

    def getNaturalScroll(self):
        return self.ifc_properties.Get(self.interface,
                                       self.NaturalScroll)

    def setNaturalScroll(self, bool_value):
        self.ifc_properties.Set(self.interface, self.NaturalScroll,
                                bool_value)

    def getMotionAcceleration(self):
        return self.ifc_properties.Get(self.interface,
                                       self.MotionAcceleration)

    def setMotionAcceleration(self, double_value):
        """
double MouseWorker::converToMotionAcceleration(int value)
{
    switch (value) {
    case 0:
        return 3.2;
    case 1:
        return 2.3;
    case 2:
        return 1.6;
    case 3:
        return 1.0;
    case 4:
        return 0.6;
    case 5:
        return 0.3;
    case 6:
        return 0.2;
    default:
        return 1.0;
    }
}
        """
        self.ifc_properties.Set(self.interface, self.MotionAcceleration,
                                double_value)

    def getDoubleClick(self):
        return self.ifc_properties.Get(self.interface,
                                       self.DoubleClick)

    def setDoubleClick(self, int_value):
        """
int MouseWorker::converToDouble(int value)
{
    return 800 - value * 100;
}
        """
        self.ifc_properties.Set(self.interface, self.DoubleClick,
                                int_value)
