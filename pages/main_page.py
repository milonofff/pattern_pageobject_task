from selenium.common import NoAlertPresentException
"""
NoAlertPresentException — используется для обработки ситуации,
когда всплывающего алерта (alert) не существует, и вызов .switch_to.alert вызвал бы ошибку.
"""
from .base_page import BasePage
"""
BasePage — это родительский класс, содержащий общие методы для всех страниц 
(например, навигация по страницам, проверка элементов и т.д.).
"""
from .locators import MainPageLocators
"""
MainPageLocators — отдельный файл или класс, где хранятся селекторы 
(например, ID, XPath или CSS-селекторы) для элементов страницы.
"""

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    # Два метода перехода на главную страницу логина и проверки ссылки на наличие логина мы передали в base_page
    # def go_to_login_page(self): # метод для перехода на страницу логина.
    #     login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
    #     """
    #     self.browser — экземпляр браузера (например, Chrome или Firefox), переданный из BasePage.
    #     MainPageLocators.LOGIN_LINK — локатор, указывающий на ссылку для входа.
    #     * — распаковка кортежа локатора (например, ("id", "login_link")).
    #     """
    #     login_link.click() # Клик по ссылке на логин.
    #
    #     try: # Обработка всплывающего окна (alert)
    #         alert = self.browser.switch_to.alert
    #         """
    #         .switch_to.alert — переключается на открывшееся всплывающее окно.
    #         .accept() — нажимает на кнопку "ОК" в алерте.
    #         """
    #         alert.accept()
    #     except NoAlertPresentException:
    #         """
    #         Обработка исключения — если алерт не появился, исключение NoAlertPresentException
    #         предотвратит падение теста. Вместо этого выведется сообщение "Alert не появился, продолжаем тест"
    #         """
    #         print("Alert не появился, продолжаем тест")
    #     #return LoginPage(browser=self.browser, url=self.browser.current_url)
    #
    # def should_be_login_link(self): # проверяет наличие ссылки на логин
    #     """
    #     self.is_element_present() — метод (предположительно из BasePage),
    #     который проверяет наличие элемента на странице.
    #     "Login link is not presented" — сообщение, которое появится в случае ошибки.
    #     """
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"



