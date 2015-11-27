"""
Remember:
    setUp: always will run before one test_ function in my Testcase
    tearDown: always will run after one test_ function in my Testcase
"""

from django.test import TestCase
from first.lib import calc


class TestCalcLib(TestCase):

    def setUp(self):
        print 'setUp ...'

    def tearDown(self):
        print 'tearDown ...'

    def test_first_name1(self):
        soma = calc(1, 2)
        self.assertEqual(soma, 3, msg='Coisa')

    def test_first_name2(self):
        soma = calc(1, 3)
        self.assertEqual(soma, 4)
