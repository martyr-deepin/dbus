#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import sys
import test_session_bus_daemon_Dock_dde_dock_DockSetting
import testSessionBusDesktop
import testSessionBusLauncher
import testSessionBusLauncherSetting


suite1 = test_session_bus_daemon_Dock_dde_dock_DockSetting.suite()
suite2 = testSessionBusLauncher.suite()
suite3 = testSessionBusDesktop.suite()
suite4 = testSessionBusLauncherSetting.suite()
alltests = unittest.TestSuite((suite1,suite2,suite3,suite4))

# 执行测试
def main(out=sys.stderr, verbosity=2):
	unittest.TextTestRunner(out,verbosity=verbosity).run(alltests)

if __name__ == '__main__':
	with open('test.result', 'w') as f:
		main(f)
'''
runner = unittest.TextTestRunner()
runner.run(alltests)
'''