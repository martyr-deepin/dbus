#!/usr/bin/python
#encoding:utf-8

import unittest 
import dbus
import time
import commands
import pexpect
import os

mypassword = 'a'
def rmlock1():

	output = pexpect.spawn('sudo rm -f /var/cache/apt/archives/lock')
	output.expect('sudo')  
	output.sendline(mypassword)  
	output.interact()

def rmlock2():

	output = pexpect.spawn('sudo rm -f /var/lib/dpkg/lock')
	output.expect('sudo')  
	output.sendline(mypassword)  
	output.interact()

class testSessionBusLauncher(unittest.TestCase):
	
	
	def setUp(self):
		self.session_bus = dbus.SessionBus()
		self.session_obj = self.session_bus.get_object('com.deepin.dde.daemon.Launcher', '/com/deepin/dde/daemon/Launcher')
		self.session_if = dbus.Interface(self.session_obj,dbus_interface='com.deepin.dde.daemon.Launcher')

	
	def tearDown(self):
		if os.path.exists('/var/cache/apt/archives/lock'):
			rmlock1()
		if os.path.exists('/var/lib/dpkg/lock'):
			rmlock2()
		output = pexpect.spawn('sudo apt-get install -y deepin-movie')
		output.expect('sudo')  
		output.sendline(mypassword)  
		time.sleep (5)
		output.interact()
		rmlock2()
		language = os.environ.get('LANGUAGE')
		if 'en' in language:
			install = commands.getoutput('aptitude show deepin-movie |awk \'/State/{print $2}\'')
			self.assertEqual(install,'installed')

		else:
			install = commands.getoutput('aptitude show deepin-movie |awk \'/状态/{print $2}\'')
			self.assertEqual(install,'已安装')
	
	

	#precondition:need install xmind from deepin-appstore
	def testComDeepinDdeDaemonLauncher(self):
		
		sendtodesktop = self.session_if.RequestSendToDesktop('deepin-movie')
		time.sleep (5)
		self.assertTrue(sendtodesktop)
		
		IsItemOnDesktop = self.session_if.IsItemOnDesktop('deepin-movie')
		time.sleep (5)
		self.assertTrue(IsItemOnDesktop)

		removefromdesktop = self.session_if.RequestRemoveFromDesktop('deepin-movie')
		time.sleep (5)
		self.assertTrue(removefromdesktop)
		
		uninstall = self.session_if.RequestUninstall('deepin-movie',1)
		time.sleep (10)
		self.assertIsNone(uninstall)


def suite():
	suite = unittest.TestSuite()
	suite.addTest(testSessionBusLauncher('testComDeepinDdeDaemonLauncher'))
	return suite

if __name__ == '__main__':
	unittest.main(defaultTest='suite')
