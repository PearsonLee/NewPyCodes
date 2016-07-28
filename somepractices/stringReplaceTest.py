# -*- coding: utf-8 -*-

import string
import os.path
import os
import datetime
import time


def replaceString():
    now = datetime.datetime.fromtimestamp(time.time()).strftime("%H:%M:%S")
    startT = datetime.datetime.fromtimestamp(time.time() + 30).strftime(
        "%H:%M:%S")
    endT = datetime.datetime.fromtimestamp(time.time() + 35).strftime(
        "%H:%M:%S")
    print now, startT, endT
    touchRuntime = open(os.getcwd() + "runtime.yml", "w")
    testString = """
-runtim:
    check: 1
    startTime: "%s"
    entTime: "%s"
""" % (startT, endT)
    touchRuntime.write(testString)


if __name__ == '__main__':
    replaceString()
