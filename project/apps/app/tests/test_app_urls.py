from django.test import TestCase
from django.urls import resolve, reverse


class AppURLsTest(TestCase):
    def test_if_url_app_is_correct(self):
        self.assertEqual(reverse('app'), '/app/')

    def test_if_url_app_render_correct_view(self):
        self.assertEqual(resolve('/app/').func.__name__, 'app')

    def test_if_url_app_return_status_code_200(self):
        ...

    def test_if_url_app_signup_is_correct(self):
        self.assertEqual(reverse('signup'), '/app/signup/')

    def test_if_url_app_signup_render_correct_view(self):
        self.assertEqual(resolve('/app/signup/').func.__name__, 'signup')

    def test_if_url_app_signup_return_status_code_200(self):
        self.assertEqual(self.client.get(reverse('signup')).status_code, 200)

    def test_if_url_app_login_is_correct(self):
        self.assertEqual(reverse('login'), '/app/login/')

    def test_if_url_app_login_render_correct_view(self):
        self.assertEqual(resolve('/app/login/').func.__name__, 'login_view')

    def test_if_url_app_login_return_status_code_200(self):
        self.assertEqual(self.client.get(reverse('login')).status_code, 200)
