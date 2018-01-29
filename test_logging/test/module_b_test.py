#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Date: 一  1/29 18:56:22 2018
"""
import sys
sys.path.append('..')
from util import module_b
import unittest

class ClassBTestCase(unittest.TestCase):
    def test_method(self):
        classb = module_b.ClassB()
        self.assertTrue(classb.method())

if __name__ == "__main__":
    unittest.main()
