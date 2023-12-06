from selenium.webdriver.common.by import By

from project.utils.testing import FunctionalTestBase


class AppFunctionalTest(FunctionalTestBase):
    def test_if_get_view_app_redirect_for_login_page(self):
        content = self.get_content('body', url='/app/')
        self.assertIn('Poupy', content.text)
        self.assertIn('Access the platform', content.text)
        self.assertIn('Username', content.text)
        self.assertIn('Password', content.text)
        self.assertIn("Don't have an account? Register", content.text)
        self.assertIn('Login', content.text)

    def test_signup_an_login_user_and_if_page_presents_correct_content_for_new_user(
        self,
    ):
        # In register page
        user = self.user_register()

        # In login page
        self.login(user['username'], user['password'])

        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('Tester', body.text)
        self.assertIn('Hello, Tester!', body.text)
        self.assertIn('Monthly income', body.text)
        self.assertIn('Monthly expenses', body.text)
        self.assertIn('Total balance', body.text)
        self.assertIn(
            "It looks like you don't have any accounts yet.", body.text
        )

        header = self.browser.find_element(By.TAG_NAME, 'header')
        self.assertIn('HOME', header.text)
        self.assertIn('ACCOUNTS', header.text)
        self.assertIn('TRANSACTIONS', header.text)
