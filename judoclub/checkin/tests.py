"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
This line is added for testing
This line added from zhaoyu.johnny@gmail.com
Replace this with more appropriate tests for your application.
"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
