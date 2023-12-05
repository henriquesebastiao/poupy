from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from project.utils.testing import AppMixin, FunctionalTestBase


class AppFunctionalTest(FunctionalTestBase, AppMixin):
    def test_if_get_view_app_redirect_for_login_page(self):
        content = self.get_content('body', url='/app/')
        self.assertIn('Poupy', content.text)
        self.assertIn('Access the platform', content.text)
        self.assertIn('Username', content.text)
        self.assertIn('Password', content.text)
        self.assertIn("Don't have an account? Register", content.text)
        self.assertIn('Login', content.text)

    def test_signup_an_login_user(self):
        # User open page
        self.browser.get(self.live_server_url + '/app/signup/')

        inputs = [
            ['Enter your first name', 'Tester'],
            ['Enter your last name', 'Last'],
            ['Enter a username', 'test_username'],
            ['Enter your best email', 'test@email.com'],
            ['Enter a secure password', 'Test@123'],
            ['Enter your password again', 'Test@123'],
        ]

        for item in inputs:
            # You see an input field with the text "Enter your first name"
            signup_inputs = self.browser.find_element(
                By.XPATH, f'//input[@placeholder="{item[0]}"]'
            )
            # Input first name
            signup_inputs.send_keys(item[1])
            # Go to next input
            signup_inputs.send_keys(Keys.TAB)

            # Verify if is last repeat and press enter
            if item[0] == inputs[5][0]:
                signup_inputs.send_keys(Keys.ENTER)

        # In login page
        # Input username
        username_input = self.browser.find_element(
            By.XPATH, '//input[@placeholder="Enter your username"]'
        )
        username_input.send_keys('test_username')
        username_input.send_keys(Keys.TAB)

        # Input password
        password_input = self.browser.find_element(
            By.XPATH, '//input[@placeholder="Enter your password"]'
        )
        password_input.send_keys('Test@123')
        password_input.send_keys(Keys.TAB)
        password_input.send_keys(Keys.ENTER)

        self.assertIn(
            'Tester', self.browser.find_element(By.TAG_NAME, 'body').text
        )
