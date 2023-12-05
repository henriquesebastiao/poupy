from project.utils.testing import AppMixin, FunctionalTestBase


class WebsiteHomePageFunctionalTest(FunctionalTestBase, AppMixin):
    def test_if_website_home_page_contain_correct_content(self):
        content = self.get_content('body')
        self.assertIn(
            'Gerencie suas finanças de forma simples e eficiente.',
            content.text,
        )
        self.assertIn(
            'Poupy é um sistema de controle financeiro pessoal que permite que você '
            'gerencie suas finanças de forma simples e eficiente.',
            content.text,
        )
