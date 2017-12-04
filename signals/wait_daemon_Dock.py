#!/usr/bin/env python3
# -*- coding: utf-8

import pexpect

class WaitSignalMonitorDaemonDock:
    def run(self):
        child = pexpect.spawn("python3 signals/signal_daemon_Dock.py")
        i = child.expect(["DaemonDock", pexpect.EOF, pexpect.TIMEOUT], 5)

        if i == 0:
            True
        else:
            False

if __name__ == "__main__":
    wait = WaitSignalMonitorDaemonDock()
    wait.run()
