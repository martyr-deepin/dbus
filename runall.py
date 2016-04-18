#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
import test_session_bus_daemon_Dock_dde_dock_DockSetting

suite1 = test_session_bus_daemon_Dock_dde_dock_DockSetting.suite()

alltests = unittest.TestSuite((suite1))

# 执行测试
runner = unittest.TextTestRunner()
runner.run(alltests)
