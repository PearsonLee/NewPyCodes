# -*- coding: utf-8 -*-

"""
Regression testing framework

This module will search for scripts in the same directory named xxxtest.py
Each such script should be a test suite that tests a module through unittest.
This script will aggregate all found test suites into one big test suite and
run them all at once.
"""

import sys
import os
import re
import unittest


def regression_test():
    # path = os.path.abspath(os.path.dirname(sys.argv[0]))  # 这样是将获取脚本所在路径
    path = os.getcwd()
    sys.path.append(path)  # 这两行是获取测试用例模块所在路径，好处是不一定要将脚本与测试用例放在同一目录中，
    files = os.listdir(path)
    test = re.compile("test\.py$", re.IGNORECASE)
    files = filter(test.search, files)
    filename_to_moudle_name = lambda f: os.path.splitext(f)[0]
    module_names = map(filename_to_moudle_name, files)
    modules = map(__import__, module_names)
    load = unittest.defaultTestLoader.loadTestsFromModule
    return unittest.TestSuite(map(load, modules))


if __name__ == '__main__':
    unittest.main(defaultTest="regression_test")
