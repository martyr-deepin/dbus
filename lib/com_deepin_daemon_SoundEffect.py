#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import os
import dbus

class DbusSoundEffect:
    def __init__(self):
        self.dbus_name = "com.deepin.daemon.SoundEffect"
        self.obj_path = "/com/deepin/daemon/SoundEffect"
        self.interface = "com.deepin.daemon.SoundEffect"

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.obj_path)
        self.ifc_properties = dbus.Interface(self.session_obj,

                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods    = dbus.Interface(self.session_obj,
                dbus_interface=self.interface)

        self.EventPowerPlug     = "power-plug"
        self.EventPowerUnplug   = "power-unplug"
        self.EventBatteryLow    = "power-unplug-battery-low"
        self.EventVolumeChanged = "audio-volume-change"
        self.EventIconToDesktop = "x-deepin-app-sent-to-desktop"
        self.EventShutdown      = "system-shutdown"
        self.EventWakeup        = "suspend-resume"

        self.EventPowerUnplugBatteryLow   = "power-unplug-battery-low"
        self.EventAudioVolumeChanged      = "audio-volume-change"
        self.EventXDeepinAppSentToDesktop = "x-deepin-app-sent-to-desktop"
        self.EventDesktopLogin            = "desktop-login"
        self.EventDesktopLogout           = "desktop-logout"
        self.EventSystemShutdown          = "system-shutdown"
        self.EventSuspendResume           = "suspend-resume"

        self.EventDeviceAdded   = "device-added"
        self.EventDeviceRemoved = "device-removed"

        self.EventTrashEmpty    = "trash-empty"
        self.EventCameraShutter = "camera-shutter"
        self.EventMessage       = "message"
        self.EventCompleteCopy  = "complete-copy"
        self.EventCompletePrint = "complete-print"

        self.EventDialogErrorCritical = "dialog-error-critical"
        self.EventDialogError         = "dialog-error"
        self.EventDialogErrorSerious  = "dialog-error-serious"

        self.EventScreenCaptureComplete = "screen-capture-complete"
        self.EventScreenCapture = "screen-capture"

        self.EventList = [self.EventPowerPlug,
                          self.EventPowerUnplug,
                          self.EventBatteryLow,
                          self.EventVolumeChanged,
                          self.EventIconToDesktop,
                          self.EventShutdown,
                          self.EventWakeup,
                          self.EventPowerUnplugBatteryLow,
                          self.EventAudioVolumeChanged,
                          self.EventXDeepinAppSentToDesktop,
                          self.EventDesktopLogin,
                          self.EventDesktopLogout,
                          self.EventSystemShutdown,
                          self.EventSuspendResume,
                          self.EventDeviceAdded,
                          self.EventDeviceRemoved,
                          self.EventTrashEmpty,
                          self.EventCameraShutter,
                          self.EventMessage,
                          self.EventCompleteCopy,
                          self.EventCompletePrint,
                          self.EventDialogErrorCritical,
                          self.EventDialogError,
                          self.EventDialogErrorSerious,
                          self.EventScreenCaptureComplete,
                          self.EventScreenCapture]


    def PlaySystemSound(self, event_type):
        try:
            self.ifc_methods.PlaySystemSound(event_type)
            return True
        except:
            return False
