#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

cache_signal_file = 'signal.txt'

class Utils:
    def clearCache():
        if os.path.exists(cache_signal_file):
            os.remove(cache_signal_file)

    def readSignalFile():
        if os.path.exists(cache_signal_file):
            with open(cache_signal_file, 'r') as f:
                content = f.readline()
                if len(content) > 0:
                    return content
                else:
                    return None
