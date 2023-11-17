from django.test import TestCase
from django.urls import reverse


class WebsiteViewsTest(TestCase):
    def test_if_view_home_load_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'pages/website/home.html')
