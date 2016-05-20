#!/usr/bin/python
#encoding=utf-8

import unittest 
import dbus
import time


class testSessionBusLauncherSetting(unittest.TestCase):
	@classmethod
	def setUpClass(cl):
		cl.session_bus = dbus.SessionBus()
		cl.session_obj = cl.session_bus.get_object('com.deepin.dde.daemon.Launcher',
													'/com/deepin/dde/daemon/Launcher')
		cl.session_if = dbus.Interface(cl.session_obj,dbus_interface='com.deepin.dde.daemon.launcher.Setting')

	

	def testComDeepinDdeDaemonLauncherSetting(self):
		#SetCategoryDisplayMode() and GetCategoryDisplayMode() were discarded
		#only SetSortMethod() and GetSortMethod() are useful
		#sort by icon and text are both 1L
		int64_list = [0L,1L,2L,3L]
		for x in int64_list:
			time.sleep (2)
			sortmethod = self.session_if.SetSortMethod(x)
			print self.session_if.GetSortMethod()
			self.assertEqual(self.session_if.GetSortMethod(),x)
			
	@classmethod
	def tearDownClass(cl):
		cl.session_if.SetSortMethod(0L)
		time.sleep (5)
		print "now launcher is sort by %s" % cl.session_if.GetSortMethod()


def suite():
	suite = unittest.TestSuite()
	suite.addTest(testSessionBusLauncherSetting('testComDeepinDdeDaemonLauncherSetting'))
	return suite

if __name__ == '__main__':
	unittest.main(defaultTest='suite')
