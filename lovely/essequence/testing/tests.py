import pprint
import unittest
import doctest

from . import layer


def setUp(test):
    test.globs['crate_port'] = layer.port
    test.globs['pprint'] = pprint.pprint


def create_suite(testfile,
                 layer=layer.crate_layer,
                 level=None,
                 setUp=setUp,
                 tearDown=None,
                 cls=doctest.DocFileSuite, encoding='utf-8'):
    suite = cls(
        testfile, tearDown=tearDown, setUp=setUp,
        optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS,
        encoding=encoding)
    if layer:
        suite.layer = layer
    if level:
        suite.level = level
    return suite


def test_suite():
    s = unittest.TestSuite((
        create_suite('../../../README.rst'),
    ))
    return s
