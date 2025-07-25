from django.test import TestCase
from django.urls import reverse


class WebsiteTemplatesTest(TestCase):
    def test_if_template_contain_correct_itens(self):
        html = self.client.get(reverse('home')).content.decode('utf8')
        self.assertIn('Gerencie suas finanças de forma simples e eficiente.', html)
        self.assertIn(
            'Poupy é um sistema de controle financeiro pessoal que permite que você\n                gerencie suas finanças de forma simples e eficiente.',
            html,
        )
