# -*- coding: utf-8 -*-
import os

from unittest import TestSuite, TestLoader


def test_suite():
    suite = TestSuite()
    tests = TestLoader().discover(start_dir=os.path.dirname(__file__))
    suite.addTests(tests)
    return suite