#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dbus

class DbusMime:
    def __init__(self):
        self.dbus_name = 'com.deepin.daemon.Mime'
        self.dbus_path = '/com/deepin/daemon/Mime'
        self.dbus_ifc  = 'com.deepin.daemon.Mime'

        self.session_bus = dbus.SessionBus()
        self.session_obj = self.session_bus.get_object(self.dbus_name,
                self.dbus_path)
        self.ifc_properties = dbus.Interface(self.session_obj,
                dbus_interface=dbus.PROPERTIES_IFACE)
        self.ifc_methods = dbus.Interface(self.session_obj,
                dbus_interface=self.dbus_ifc)

        self.mimetype_Browser = 'x-scheme-handler/http'
        self.mimetype_Mail = 'x-scheme-handler/mailto'
        self.mimetype_Text = 'text/plain'
        self.mimetype_Music = 'audio/mpeg'
        self.mimetype_Video = 'video/mp4'
        self.mimetype_Picture = 'image/jpeg'
        self.mimetype_Terminal = 'application/x-terminal'
        self.mimetype_Error = 'testdefault'

    def GetDefaultApp(self, mimetype):
        """
        mimetype:
        Browser             x-scheme-handler/http
        Mail                x-scheme-handler/mailto
        Text                text/plain
        Music               audio/mpeg
        Video               video/mp4
        Picture             image/jpeg
        Terminal            application/x-Terminal
        default             ''
        """
        return self.ifc_methods.GetDefaultApp(mimetype)
