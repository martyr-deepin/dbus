#!/usr/bin/python3 env
# -*- coding: utf-8 -*-

from gi.repository import Gio

class SchemaLauncher:
    def __init__(self):
        self.gsSchemaLauncher        = "com.deepin.dde.launcher"
        self.gsKeyDisplayMode        = "display-mode"
        self.gsKeyFullscreen         = "fullscreen"
        self.gsKeyAppsUseProxy       = "apps-use-proxy"
        self.gsKeyAppsDisableScaling = "apps-disable-scaling"
        self.gsKeyAppsHidden         = "apps-hidden"
        self.schema = Gio.Settings.new(self.gsSchemaLauncher)

    def getKeyDisplayMode(self):
        return self.schema.get_value(self.gsKeyDisplayMode)

    def getKeyFullscreen(self):
        return self.schema.get_value(self.gsKeyFullscreen)

    def getKeyAppsUseProxy(self):
        return self.schema.get_value(self.gsKeyAppsUseProxy)

    def getKeyDisableScaling(self):
        return self.schema.get_value(self.gsKeyAppsDisableScaling)

    def getKeyAppsHidden(self):
        return self.schema.get_value(self.gsKeyAppsHidden)

