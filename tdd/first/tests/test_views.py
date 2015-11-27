"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User


class TestUserLogin(TestCase):

    def setUp(self):
        # create user
        self.user = User.objects.create(username='test1')
        # set password
        self.user.set_password('test1')
        self.user.save()

    def test_basic_login(self):
        """
        do the login
        """
        login = self.client.login(user='test1', password='test1')
        self.assertIn('_auth_user_id', self.client.session)
        self.assertTrue(login)

    def test_basic_logout(self):
        """
        do the logout
        """
        self.client.logout()
        self.assertNotIn('_auth_user_id', self.client.session)
