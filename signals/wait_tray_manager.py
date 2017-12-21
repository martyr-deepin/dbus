#!/usr/bin/env python3
# -*- coding: utf-8

import pexpect

class WaitSignalMonitorTrayManager:
    def run(self):
        child = pexpect.spawn("python3 signals/signal_tray_manager.py")
        i = child.expect(["TrayManager", pexpect.EOF, pexpect.TIMEOUT], 30)

        if i == 0:
            True
        else:
            False

if __name__ == "__main__":
    wait = WaitSignalMonitorTrayManager()
    wait.run()
