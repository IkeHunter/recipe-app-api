"""
Test for the Django admin modifications
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """Tests for Django admin."""

    def setUp(self):  # diff capitalize convention for py unit test
        """Create user and client."""
        self.client = Client()
        # Create super user to authenticate new base user
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        # force authentication to this user
        self.client.force_login(self.admin_user)
        # Create normal user as test
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test User'
        )

    def test_users_list(self):
        """Test that users are listed on page."""
        # which url we pull from django admin, page that lists users
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)  # http request to url

        self.assertContains(res, self.user.name)  # page contains name
        self.assertContains(res, self.user.email)  # page contains email

    def test_edit_user_page(self):
        """Test the edit user page works."""
        # url for change user page
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test create user page."""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
