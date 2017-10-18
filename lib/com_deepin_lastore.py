#!/usr/bin/env python3
#-*- coding=utf-8 -*-

import dbus

class Lastore:
    def __init__(self):
        self.servicename = 'com.deepin.lastore'
        self.path = '/com/deepin/lastore'
        self.method = 'com.deepin.lastore.Manager'

        self.systembus = dbus.Systembus()
        self.systemobj = self.systembus.getobject(self.servicename, self.path)
  
        self.ifc_properties = dbus.Interface(self.system_obj, dbus_interface = dbus.PROPERTIES_IFACE)
        self.ifc_method     = dbus.Interface(self.system_obj, dbus_interface = self.method)

        self.properties_SystemArchitectures = 'SystemArchitectures'
        self.properties_UpgradableApps = 'UpgradableApps'


    def InstallPackage(self, short_pkgname, pkgname):
        '''
        第一个参数可以传空，是给右上角气泡提示用的，比如安装包abcdefg后，提示名为abc
        可直接使用命令安装
        lastore-tools test -j install seamonkey
        '''
        return self.ifc_method.InstallPackage(short_pkgname, pkgname)

    def PackageDesktop(self, pkgname):
        '''
        返回安装包的desktop文件路径，比如传入'birdfont',返回'/usr/share/applications/birdfont.desktop'
        可直接使用命令返回结果
        qdbus --system com.deepin.lastore /com/deepin/lastore com.deepin.lastore.Manager.PackageDesktopPath 'birdfont'
        '''
        return self.ifc_method.PackageDesktop(pkgname)

    def PackageExists(self, pkgname):
        '''
        返回True/False，如果包存在则返回True，包不存在则返回False
        '''
        return self.ifc_method.PackageExists(pkgname)

    def PackageInstallable(self, pkgname):
        '''
        返回True/False，如果包可以安装则返回True，包不可以安装则返回False，比如abcdefgh是不可以安装的
        '''
        return self.ifc_method.PackageInstallable(pkgname)

    def PackageDownloadSize(self, *pkglist):
        '''
        返回根据当前cache所需要的实际下载大小
        '''
        return self.ifc_method.PackageSownloadSize(*pkglist)

    def RemovePackage(self, short_pkgname, pkgname):
        '''
        第一个参数可以传空，是给右上角气泡提示用的，比如删除包abcdefg后，提示名为abc
        可直接使用命令安装
        lastore-tools test -j remove seamonkey
        '''
        return self.ifc_method.RemovePackage(short_pkgname, pkgname)

    def GetSystemArchitectures(self):
        '''
        返回系统架构['amd64', 'i386']
        '''
        return self.ifc_properties.Get(self.method, self.properties_SystemArchitectures)

    def GetUpgradableApps(self):
        '''
        返回可更新的包
        '''      
        return self.ifc_properties.Get(self.method, self.properties_UpgradableApps)
