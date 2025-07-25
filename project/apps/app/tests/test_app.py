from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import resolve, reverse


class AppTest(TestCase):
    def test_if_url_app_is_correct(self):
        self.assertEqual(reverse('app'), '/app/')

    def test_if_url_app_render_correct_view(self):
        self.assertEqual(resolve('/app/').view_name, 'app')

    def test_if_url_app_return_status_code_200(self):
        User.objects.create_user(username='test_user', password='test_password')
        self.client.login(username='test_user', password='test_password')
        self.assertEqual(self.client.get(reverse('app')).status_code, 200)

    def test_if_view_app_load_correct_template(self):
        User.objects.create_user(username='test_user', password='test_password')
        self.client.login(username='test_user', password='test_password')

        self.assertTemplateUsed(self.client.get(reverse('app')), 'pages/app/home.html')
