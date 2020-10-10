import unittest

from contract import contract, gt, validvalues, gteq, lt, lteq, closed, opened, closedopened, openedclosed, checktype
from unittest import TestCase, TestSuite, main

class Simple(object):
    @contract({})
    def __init__(self):
        pass

    @classmethod
    @contract({})
    def cm(cls, a, b):
        pass

    @staticmethod
    @contract({})
    def sm(a, b):
        pass

    @contract({})
    def m(self, a, b):
        pass

    @contract({})
    def t(this, a, b):
        pass


@contract({'a': [gt(0)]})
def m(a, b):
    pass

class ContractTestCase(TestCase):

    def test_method_check(self):
        m(7, 8)

    def test_method_exception_check(self):
        with self.assertRaises(AssertionError):
            m(-7, 8)

    def test_class_constructor(self):
        Simple()

    def test_class_instance_method(self):
        s = Simple()
        s.m(5, 6)

    def test_class_static_method(self):
        s = Simple()
        s.sm(3, 4)

    def test_class_class_method(self):
        s = Simple()
        s.cm(1, 2)

    def test_class_instance_method_with_this_self(self):
        s = Simple()
        s.t(9, 10)

colors = ['blue','red','yellow','green']

class ValidateObject(object):

    def __init__(self):
        pass

    @contract({'c':[validvalues(colors)]})
    def get_color(self,c):
        pass

    @contract({'a':[gt(1)]})
    def check_gt(self,a):
        pass

    @contract({'a':[gteq(1)]})
    def check_gteq(self,a):
        pass

    @contract({'a':[lt(1)]})
    def check_lt(self,a):
        pass

    @contract({'a':[lteq(1)]})
    def check_lteq(self,a):
        pass

    @contract({'a':[checktype(int)]})
    def check_checktype(self,a):
        pass

    @contract({'a':[closed(1,3)]})
    def check_closed(self,a):
        pass

    @contract({'a':[opened(1,3)]})
    def check_opened(self,a):
        pass

    @contract({'a':[closedopened(1,3)]})
    def check_closedopened(self,a):
        pass

    @contract({'a':[openedclosed(1,3)]})
    def check_openedclosed(self,a):
        pass

@contract({'b':[checktype(int)]})
def non_existent_parameter_name(a):
    pass

class InvalidContractTestCase(TestCase):

    def test_not_using_tuple(self):
        with self.assertRaises(AssertionError):
            @contract({'a': opened(0, 7)})
            def not_using_tuple(a):
                pass

    def test_non_existent_parameter_name(self):
        non_existent_parameter_name(101)

    def test_invalid_type(self):
        with self.assertRaises(AssertionError):
            @contract({'a':[checktype(int), lt(5)]})
            def not_valid_type_call(a):
                pass

            not_valid_type_call(1.34)

class DecoratorOptionTestCase(TestCase):
    """
    This test will just test that the different decorator options
    are recognized and valid.

    It currently test the following options:

        - validvalues
        - checktype
        - closed
        - opened
        - closedopened
        - openedclosed
        - gt
        - lt
        - gteq
        - lteq
    """
    def setUp(self):
        self.v = ValidateObject()

    def test_validvalues(self):
        self.v.get_color('green')

    def test_checktype(self):
        self.v.check_checktype(101)

    def test_closed(self):
        self.v.check_closed(1)

    def test_opened(self):
        self.v.check_opened(1.2)

    def test_closedopened(self):
        self.v.check_closedopened(1)

    def test_openedclosed(self):
        self.v.check_openedclosed(3)

    def test_gt(self):
        self.v.check_gt(11)

    def test_gteq(self):
        self.v.check_gteq(1)

    def test_lt(self):
        self.v.check_lt(0)

    def test_invalid_lt(self):
        with self.assertRaises(AssertionError):
            self.v.check_lt(1)

    def test_lteq(self):
        self.v.check_lteq(1)

    def test_invalid_lteq(self):
        with self.assertRaises(AssertionError):
            self.v.check_lteq(5)

def load_tests(loader, tests, pattern):
    """
    The unittest module looks for this method within a module
    and provides it the necessary instances to add tests too.
    We just need to insure that we set the module name to this
    file module name.
    """
    test_classes = [ ContractTestCase, DecoratorOptionTestCase, InvalidContractTestCase ]

    suite = TestSuite()
    for test_class in test_classes:
        suite.addTests(loader.loadTestsFromTestCase(test_class))
    return suite

if (__name__ == '__main__'):
    unittest.main(module=__name__, exit=False)
