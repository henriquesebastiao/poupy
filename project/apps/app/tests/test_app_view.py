from django.test import TestCase
from django.urls import reverse


class AppViewsTest(TestCase):
    def test_if_view_app_load_correct_template(self):
        ...

    def test_if_view_signup_load_correct_template(self):
        self.assertTemplateUsed(
            self.client.get(reverse('signup')), 'pages/app/signup.html'
        )

    def test_if_view_login_load_correct_template(self):
        self.assertTemplateUsed(
            self.client.get(reverse('login')), 'pages/app/login.html'
        )
