#!/usr/bin/python
#encoding=utf-8

import unittest 
import dbus
import time

class testSessionBusLauncher(unittest.TestCase):
	@classmethod
	def setUpClass(cl):
		cl.session_bus = dbus.SessionBus()
		cl.session_obj1 = cl.session_bus.get_object('com.deepin.dde.daemon.Launcher',
													'/com/deepin/dde/daemon/Launcher')
		cl.session_if1 = dbus.Interface(cl.session_obj1,dbus_interface='com.deepin.dde.daemon.Launcher')

	#precondition:need install xmind from deepin-appstore
	def testComDeepinDdeDaemonLauncher(self):
		
		sendtodesktop = self.session_if1.RequestSendToDesktop('xmind')
		time.sleep (5)
		self.assertTrue(sendtodesktop)
		
		IsItemOnDesktop = self.session_if1.IsItemOnDesktop('xmind')
		time.sleep (5)
		self.assertTrue(IsItemOnDesktop)

		removefromdesktop = self.session_if1.RequestRemoveFromDesktop('xmind')
		time.sleep (5)
		self.assertTrue(removefromdesktop)
		
		uninstall = self.session_if1.RequestUninstall('xmind',1)
		time.sleep (10)
		self.assertIsNone(uninstall)


	def testComDeepinDdeDaemonLauncherSetting(self):
		displaymode = self.session_if2.SetCategoryDisplayMode(2L)
		print self.session_if2.GetCategoryDisplayMode()
		sortmethod = self.session_if2.SetSortMethod(1L)
		print self.session_if2.GetSortMethod()



def suite():
	suite = unittest.TestSuite()
	suite.addTest(testSessionBusLauncher('testComDeepinDdeDaemonLauncher'))
	#suite.addTest(testSessionBusLauncher('testComDeepinDdeDaemonLauncherSetting'))
	return suite

if __name__ == '__main__':
	unittest.main(defaultTest='suite')
