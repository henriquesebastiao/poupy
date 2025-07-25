from django.test import TestCase
from django.urls import reverse


class UserCreateTest(TestCase):
    def test_if_url_user_creat_method_get_return_404(self):
        self.assertEqual(self.client.get(reverse('user_create')).status_code, 404)
