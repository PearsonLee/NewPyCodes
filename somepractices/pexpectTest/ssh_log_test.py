#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pexpect
import sys

child = pexpect.spawn('ssh root@192.168.182.133')
fout = open('mylog.txt', 'w')
child.logfile = fout

child.expect("password:")
child.sendline('toor')
child.expect('#')
child.sendline('ls /home')
child.expect('#')
