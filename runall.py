#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import test_session_bus_daemon_Dock_dde_dock_DockSetting
import testSessionBusDesktop
import testSessionBusLauncher

suite1 = test_session_bus_daemon_Dock_dde_dock_DockSetting.suite()
suite2 = testSessionBusDesktop.suite()
suite3 = testSessionBusLauncher.suite()

alltests = unittest.TestSuite((suite1,suite2,suite3))

# 执行测试
runner = unittest.TextTestRunner()
runner.run(alltests)
