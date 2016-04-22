#!/usr/bin/python
#encoding=utf-8

import unittest 
import dbus


class testSessionBusDesktop(unittest.TestCase):
	@classmethod
	def setUpClass(cl):
		cl.session_bus = dbus.SessionBus()
		cl.session_obj = cl.session_bus.get_object('com.deepin.dde.daemon.Desktop',
													'/com/deepin/dde/daemon/Desktop')
		cl.session_if = dbus.Interface(cl.session_obj,dbus_interface='com.deepin.dde.daemon.Desktop')


	def testComDeepinDdeDaemonDesktop(self):
		
		creatappgroup = self.session_if.RequestCreatingAppGroup((u"/home/deepin1208/桌面/deepin-feedback.desktop",
			u"/home/deepin1208/桌面/deepin-movie.desktop"))
		self.assertIsNone(creatappgroup)

		mergeappgroup = self.session_if.RequestMergeIntoAppGroup((u"/home/deepin1208/桌面/eog.desktop",
			u"/home/deepin1208/桌面/.deepin_rich_dir_程序启动组"),u"/home/deepin1208/桌面/.deepin_rich_dir_程序启动组")
		self.assertIsNone(mergeappgroup)
		'''
		ActivateFileWithTimestamp = self.session_if.ActivateFileWithTimestamp(u"/home/deepin1208/桌面/all.py",("all.py"),
																				False,0,1)
		print ActivateFileWithTimestamp
		'''
		GenMenuContent = self.session_if.GenMenuContent((u"/home/deepin1208/桌面/deepin-movie.desktop",
															u"/home/deepin1208/桌面/all.py"))
		self.assertIsNotNone(GenMenuContent)
		print GenMenuContent
		
		# 1:打开 2:压缩 3：剪切 4：复制 5：没有 6：删除 7：属性
		HandleSelectedMenuItem = self.session_if.HandleSelectedMenuItem("2")
		print HandleSelectedMenuItem


def suite():
	suite = unittest.TestSuite()
	suite.addTest(testSessionBusDesktop('testComDeepinDdeDaemonDesktop'))
	return suite

if __name__ == '__main__':
	unittest.main(defaultTest='suite')
