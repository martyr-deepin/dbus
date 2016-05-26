#!/usr/bin/python
#encoding:utf-8

import unittest 
import dbus
import os
import commands
import time 
import json
import sys
import urllib

reload(sys)

sys.setdefaultencoding('utf8')


class testSessionBusDesktop(unittest.TestCase):
	@classmethod
	def setUpClass(cl):
		cl.session_bus = dbus.SessionBus()
		cl.session_obj = cl.session_bus.get_object('com.deepin.dde.daemon.Desktop', \
													'/com/deepin/dde/daemon/Desktop')
		cl.session_obj2 = cl.session_bus.get_object('com.deepin.dde.daemon.Launcher', \
													'/com/deepin/dde/daemon/Launcher')
		cl.session_if = dbus.Interface(cl.session_obj,dbus_interface='com.deepin.dde.daemon.Desktop')
		cl.session_if2 = dbus.Interface(cl.session_obj2,dbus_interface='com.deepin.dde.daemon.Launcher')

		cl.usr_home = os.path.expanduser('~')
		print "User home dir:%s\n" % cl.usr_home
		cl.user_desktop_dir = commands.getoutput("bash -c 'source ~/.config/user-dirs.dirs \
														&& echo $XDG_DESKTOP_DIR'").decode("utf-8").split("\n")
		cl.user_desktop_dir = [n for n in cl.user_desktop_dir if len(n.strip()) > 0]
		cl.user_desktop_dir = "".join(cl.user_desktop_dir)
		print "User desktop dir:%s\n" % cl.user_desktop_dir
		
		cl.touch_a = "touch %s/a.txt" % cl.user_desktop_dir
		cl.touch_b = "touch %s/b.txt" % cl.user_desktop_dir
		cl.output1 = commands.getoutput(cl.touch_a)
		cl.output2 = commands.getoutput(cl.touch_b)
		cl.a_path = "%s/a.txt" % cl.user_desktop_dir
		cl.b_path = "%s/b.txt" % cl.user_desktop_dir
		time.sleep (2)
		


	@classmethod
	def tearDownClass(cl):
		
		cl.status1,cl.output1 = commands.getstatusoutput("rm -f "+cl.user_desktop_dir+"/*")
		cl.status2,cl.output2 = commands.getstatusoutput("rm -rf "+cl.user_desktop_dir+"/.deepin_rich_dir_*")
		'''
		time.sleep (2)
		pyautogui.hotkey('alt','f4')
		
		time.sleep (5)
		pyautogui.hotkey('alt','f4')
		'''
		

	def testMenuContent(self):
		
		if os.path.exists(self.a_path) and os.path.exists(self.b_path):
			GenMenuContent = self.session_if.GenMenuContent((self.a_path,
															self.b_path))
			self.assertIsNotNone(GenMenuContent)

		else:
			print "E: a.txt and b.txt didn't exist"
		#print GenMenuContent
		
		GenMenuContent = json.JSONDecoder().decode(GenMenuContent)

		print json.dumps(GenMenuContent,indent=4,ensure_ascii=False)
		'''
		ActivateFileWithTimestamp = self.session_if.ActivateFileWithTimestamp(self.user_desktop_dir+"/b.txt",("a.txt","b.txt"),\
																			False,0,2)
		
		time.sleep (5)
		HandleSelectedMenuItem = self.session_if.HandleSelectedMenuItem("11")

		time.sleep (5)
		'''
		
	def testAppGroup(self):
		
		#send deepin-feedback deepin-movie eog to desktop
		feedback = self.session_if2.RequestSendToDesktop('deepin-feedback')
		time.sleep (5)
		self.assertTrue(feedback)
		
		movie = self.session_if2.RequestSendToDesktop('deepin-movie')
		time.sleep (5)
		self.assertTrue(movie)

		eog = self.session_if2.RequestSendToDesktop('eog')
		time.sleep (5)
		self.assertTrue(eog)
		#drag deepin-feedback towards deepin-movie 
		creatappgroup = self.session_if.RequestCreatingAppGroup((self.user_desktop_dir+"/deepin-feedback.desktop",\
			self.user_desktop_dir+"/deepin-movie.desktop"))
		self.assertIsNone(creatappgroup)
		time.sleep (5)

		#get AppGroup name
		self.user_desktop_appgroup = commands.getoutput("bash -c 'source ~/.config/user-dirs.dirs \
														&& ls -ahl $XDG_DESKTOP_DIR |grep .deepin_rich_dir_'")\
														.decode("utf-8").split("\n")
		self.user_desktop_appgroup = [n for n in self.user_desktop_appgroup if len(n.strip()) > 0]
		self.user_desktop_appgroup = "".join(self.user_desktop_appgroup)
		self.user_desktop_appgroup = str(self.user_desktop_appgroup).replace('u\'','\'').decode("unicode-escape")
		print self.user_desktop_appgroup
		self.user_desktop_appgroup = self.user_desktop_appgroup.split("  ")[1].split(" ")[7:]
		self.user_desktop_appgroup = " ".join(self.user_desktop_appgroup)
		self.user_desktop_appgroup = str(self.user_desktop_appgroup).replace('u\'','\'').decode("unicode-escape")
		print "AppGroup name is:%s\n" % self.user_desktop_appgroup
		#merge eog into AppGroup
		self.appgroup_dir = "%s/%s" % (self.user_desktop_dir,self.user_desktop_appgroup)
		print "appgroup_dir is:%s\n" % self.appgroup_dir
		mergeappgroup = self.session_if.RequestMergeIntoAppGroup((self.user_desktop_dir+"/eog.desktop",self.appgroup_dir),self.appgroup_dir)
		self.assertIsNone(mergeappgroup)
		time.sleep (5)
		

		IsAppGroup = self.session_if.IsAppGroup(self.user_desktop_appgroup)
		print "%s is AppGroup: %d "% (self.user_desktop_appgroup,IsAppGroup)

		GetDesktopItems = self.session_if.GetDesktopItems()
		print "GetDesktopItems----------------------\n"
		print json.dumps(GetDesktopItems,indent=4,ensure_ascii=False)
		
		GetAppGroupItems = self.session_if.GetAppGroupItems(self.appgroup_dir)
		print "GetAppGroupItems----------------------\n"
		print json.dumps(GetAppGroupItems,indent=4,ensure_ascii=False)
		
		GetItemInfo = self.session_if.GetItemInfo(self.appgroup_dir)
		print "GetItemInfo----------------------\n"
		print json.dumps(GetItemInfo,indent=4,ensure_ascii=False)

def suite():
	suite = unittest.TestSuite()
	suite.addTest(testSessionBusDesktop('testMenuContent'))
	suite.addTest(testSessionBusDesktop('testAppGroup'))
	return suite

if __name__ == '__main__':
	unittest.main(defaultTest='suite')
