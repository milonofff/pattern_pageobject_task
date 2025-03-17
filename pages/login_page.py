from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """Проверяет, что в URL есть подстрока 'login'"""
        assert "login" in self.browser.current_url, "URL страницы логина некорректен"

    def should_be_login_form(self):
        """Проверяет, что форма логина присутствует на странице"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина отсутствует"

    def should_be_register_form(self):
        """Проверяет, что форма регистрации присутствует на странице"""
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации отсутствует"