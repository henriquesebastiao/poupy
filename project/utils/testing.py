import time

from django.contrib.auth.models import User
from django.test.selenium import LiveServerTestCase
from pytest import mark
from selenium.webdriver.common.by import By

from project.utils.browser import make_chrome_browser


@mark.functional_test
class FunctionalTestBase(LiveServerTestCase):
    def setUp(self) -> None:
        self.browser = make_chrome_browser()
        return super().setUp()

    def tearDown(self) -> None:
        self.browser.quit()  # Is necessary to quit the browser to avoid memory leak
        return super().tearDown()

    @staticmethod
    def sleep(seconds: int = 1) -> None:
        """
        Method to sleep the browser for a while.
        Args:
            seconds: seconds to sleep the browser

        Returns:
            None
        """
        time.sleep(seconds)

    def get_content(self, html_tag_name: str, url: str = ''):
        """
        Method to get the content of an HTML tag.
        Args:
            html_tag_name: HTML tag name to get the content
            url: URL to get the content

        Returns:
            content of an HTML tag
        """
        self.browser.get(self.live_server_url + url)
        return self.browser.find_element(By.TAG_NAME, html_tag_name)


class AppMixin:
    @staticmethod
    def make_user(
        username='test_user',
        password='test_password',
        first_name='Test',
        last_name='Last',
        email='test@email.com',
    ):
        User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
