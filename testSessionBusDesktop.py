#!/usr/bin/python
#encoding:utf-8

import unittest 
import dbus
import os
import commands
import time 
import pyautogui


class testSessionBusDesktop(unittest.TestCase):
	@classmethod
	def setUpClass(cl):
		cl.session_bus = dbus.SessionBus()
		cl.session_obj = cl.session_bus.get_object('com.deepin.dde.daemon.Desktop',
													'/com/deepin/dde/daemon/Desktop')
		cl.session_obj2 = cl.session_bus.get_object('com.deepin.dde.daemon.Launcher',
													'/com/deepin/dde/daemon/Launcher')
		cl.session_if = dbus.Interface(cl.session_obj,dbus_interface='com.deepin.dde.daemon.Desktop')
		cl.session_if2 = dbus.Interface(cl.session_obj2,dbus_interface='com.deepin.dde.daemon.Launcher')

		cl.usr_home = os.path.expanduser('~')
		print cl.usr_home
		cl.status1,cl.output1 = commands.getstatusoutput("touch ~/桌面/a.txt")
		print cl.status1
		cl.status2,cl.output2 = commands.getstatusoutput("touch ~/桌面/b.txt")
		print cl.status2
		cl.a_path = cl.usr_home+u"/桌面/a.txt"
		cl.b_path = cl.usr_home+u"/桌面/b.txt"
		time.sleep (2)


	@classmethod
	def tearDownClass(cl):
		cl.status1,cl.output1 = commands.getstatusoutput("rm -f ~/桌面/a.txt")
		cl.status2,cl.output2 = commands.getstatusoutput("rm -f ~/桌面/b.txt")
		cl.status2,cl.output2 = commands.getstatusoutput("rm -rf ~/桌面/.deepin_rich_dir_程序启动组")
		time.sleep (2)
		pyautogui.hotkey('alt','f4')
		time.sleep (2)
		pyautogui.hotkey('alt','f4')
		
	def testMenuContent(self):
		
		if os.path.exists(self.a_path) and os.path.exists(self.b_path):
			GenMenuContent = self.session_if.GenMenuContent((self.usr_home+u"/桌面/a.txt",
															self.usr_home+u"/桌面/b.txt"))
			self.assertIsNotNone(GenMenuContent)
			print GenMenuContent
		else:
			print "E: a.txt and b.txt didn't exist"
		
		HandleSelectedMenuItem = self.session_if.HandleSelectedMenuItem("11")
		print HandleSelectedMenuItem
		
		
	def testAppGroup(self):

		feedback = self.session_if2.RequestSendToDesktop('deepin-feedback')
		#time.sleep (5)
		self.assertTrue(feedback)
		
		movie = self.session_if2.RequestSendToDesktop('deepin-movie')
		#time.sleep (5)
		self.assertTrue(movie)

		eog = self.session_if2.RequestSendToDesktop('eog')
		#time.sleep (5)
		self.assertTrue(eog)

		creatappgroup = self.session_if.RequestCreatingAppGroup((self.usr_home+u"/桌面/deepin-feedback.desktop",\
			self.usr_home+u"/桌面/deepin-movie.desktop"))
		self.assertIsNone(creatappgroup)
		
		mergeappgroup = self.session_if.RequestMergeIntoAppGroup((self.usr_home+u"/桌面/eog.desktop",\
			self.usr_home+u"/桌面/.deepin_rich_dir_程序启动组"),self.usr_home+u"/桌面/.deepin_rich_dir_程序启动组")
		self.assertIsNone(mergeappgroup)
		
		ActivateFileWithTimestamp = self.session_if.ActivateFileWithTimestamp(self.usr_home+u"/桌面/b.txt",("a.txt","b.txt"),\
																				False,0,2)
		print ActivateFileWithTimestamp

	

def suite():
	suite = unittest.TestSuite()
	suite.addTest(testSessionBusDesktop('testMenuContent'))
	suite.addTest(testSessionBusDesktop('testAppGroup'))
	return suite

if __name__ == '__main__':
	unittest.main(defaultTest='suite')
