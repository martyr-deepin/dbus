#!/usr/bin/python
#encoding=utf-8

import unittest 
import dbus
import time
import commands
import pexpect
import os

mypassword = 'a'
language = os.environ['LANGUAGE']

class testSessionBusLauncher(unittest.TestCase):

	def setUp(self):
		self.session_bus = dbus.SessionBus()
		self.session_obj1 = self.session_bus.get_object('com.deepin.dde.daemon.Launcher',
													'/com/deepin/dde/daemon/Launcher')
		self.session_if1 = dbus.Interface(self.session_obj1,dbus_interface='com.deepin.dde.daemon.Launcher')


	def tearDown(self):
		self.output = pexpect.spawn('sudo apt-get install -y deepin-movie')
		self.output.expect('sudo')  
		self.output.sendline(mypassword)  
		self.output.interact()
		if 'en' in language:
			self.install = commands.getoutput('aptitude show deepin-movie |awk \'/State/{print $2}\'')
			self.assertEqual(self.install,'installed')

		else:
			self.install = commands.getoutput('aptitude show deepin-movie |awk \'/状态/{print $2}\'')
			self.assertEqual(self.install,'已安装')


	#precondition:need install xmind from deepin-appstore
	def testComDeepinDdeDaemonLauncher(self):
		
		sendtodesktop = self.session_if1.RequestSendToDesktop('deepin-movie')
		time.sleep (5)
		self.assertTrue(sendtodesktop)
		
		IsItemOnDesktop = self.session_if1.IsItemOnDesktop('deepin-movie')
		time.sleep (5)
		self.assertTrue(IsItemOnDesktop)

		removefromdesktop = self.session_if1.RequestRemoveFromDesktop('deepin-movie')
		time.sleep (5)
		self.assertTrue(removefromdesktop)
		
		uninstall = self.session_if1.RequestUninstall('deepin-movie',1)
		time.sleep (10)
		self.assertIsNone(uninstall)


def suite():
	suite = unittest.TestSuite()
	suite.addTest(testSessionBusLauncher('testComDeepinDdeDaemonLauncher'))
	return suite

if __name__ == '__main__':
	unittest.main(defaultTest='suite')
