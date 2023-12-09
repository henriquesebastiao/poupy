from django.test import TestCase
from django.urls import resolve, reverse


class LoginTest(TestCase):
    def test_if_url_login_is_correct(self):
        self.assertEqual(reverse('login'), '/app/login/')

    def test_if_url_login_create_is_correct(self):
        self.assertEqual(reverse('login_create'), '/app/login/create/')

    def test_if_url_login_render_correct_view(self):
        self.assertEqual(resolve('/app/login/').view_name, 'login')

    def test_if_url_login_create_render_correct_view(self):
        self.assertEqual(
            resolve('/app/login/create/').view_name, 'login_create'
        )

    def test_if_url_login_return_status_code_200(self):
        self.assertEqual(self.client.get(reverse('login')).status_code, 200)

    def test_if_view_login_load_correct_template(self):
        self.assertTemplateUsed(
            self.client.get(reverse('login')), 'pages/app/login.html'
        )
