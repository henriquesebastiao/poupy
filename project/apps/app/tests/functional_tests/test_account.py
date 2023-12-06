from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from project.utils.testing import FunctionalTestBase


class AccountFunctionalTest(FunctionalTestBase):
    def test_account_registration(self):
        """Test creating an account and whether it is listed on the /app/accounts/ page"""
        # User registers and logs in
        user = self.user_register()
        self.login(user['username'], user['password'])

        # User access page of accounts
        self.browser.find_element(By.XPATH, '//a[text()="ACCOUNTS"]').click()

        # User click on button to add new account
        self.browser.find_element(
            By.XPATH, '//span[text()="Add account"]'
        ).click()

        # User digit name of new account
        account_name = self.browser.find_element(
            By.XPATH, '//input[@placeholder="Enter account name"]'
        )
        account_name.send_keys('My Bank')

        # User digite balance of new account
        balance = self.browser.find_element(
            By.XPATH, '//input[@placeholder="Enter account balance"]'
        )

        # This for loop deletes the `0.0` characters that are in the value field before inserting the actual value
        for _ in range(3):
            balance.send_keys(Keys.DELETE)

        balance.send_keys('1000')

        # User press key enter and redirect to page of accounts
        balance.send_keys(Keys.ENTER)

        body = self.browser.find_element(By.TAG_NAME, 'body')
        self.assertIn('My Bank', body.text)
        self.assertIn('R$ 1000,00', body.text)
