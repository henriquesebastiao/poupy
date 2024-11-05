from django.test import TestCase
from django.urls import resolve, reverse


class WebsiteURLsTest(TestCase):
    def test_if_url_website_home_is_correct(self):
        """Verifica se a url da página inicial do site está correta"""
        self.assertEqual(reverse('home'), '/')

    def test_if_url_website_home_render_correct_view(self):
        """
        Verifica se a url da página inicial do site renderiza a view correta
        """
        self.assertEqual(resolve('/').view_name, 'home')

    def test_if_url_website_home_return_status_code_200(self):
        """
        Verifica se uma requisição GET na raiz retorna o status code 200
        """
        self.assertEqual(self.client.get('/').status_code, 200)
