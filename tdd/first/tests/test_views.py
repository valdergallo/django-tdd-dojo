"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.contrib.auth.models import User

TEST_USER = 'test'
TEST_PASSWORD = 'test@123456789'
TEST_EMAIL = 'test@test.com'


class TestUserLogin(TestCase):
    @classmethod
    def setUpTestData(cls):
        # FINALLY
        # this is will runne just one time
        print 'FINALLY ONE DATA SETUP'
        cls.user = User.objects.create_user(username=TEST_USER,
                                            email=TEST_EMAIL,
                                            password=TEST_PASSWORD,
                                            is_staff=True,
                                            is_superuser=True)

    def test_check_is_has_user(self):
        self.assertTrue(User.objects.get(username=TEST_USER))

    def test_basic_login(self):
        """
        do the login
        """
        login = self.client.login(username=TEST_USER, password=TEST_PASSWORD)
        self.assertIn('_auth_user_id', self.client.session)
        self.assertTrue(login)

    def test_basic_logout(self):
        """
        do the logout
        """
        self.client.logout()
        self.assertNotIn('_auth_user_id', self.client.session)
