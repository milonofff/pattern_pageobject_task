from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
"""
Создается базовый класс BasePage, 
от которого будут наследоваться 
другие Page Object классы.
"""
class BasePage():
    def __init__(self, browser, url, timeout=10): #10
        self.browser = browser # это объект веб-драйвера (например, webdriver.Chrome())
        self.url = url # адрес веб-страницы, которую мы хотим открыть
        self.browser.implicitly_wait(timeout) # неявное ожидание по умолчанию, задается в секундах

    def open(self): # Этот метод просто открывает страницу по self.url в браузере, используя метод get().
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """
        Проверяет наличие элемента на странице.
        :param how: Метод поиска (например, By.ID, By.CSS_SELECTOR)
        :param what: Локатор элемента
        :return: True, если элемент найден, иначе False
        """
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):# проверяет, появился ли элемент на странице
        try:
            # Ожидаем появления элемента на странице с заданным локатором.
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            # Если по истечении времени элемент не был найден, возвращаем True (элемент не появился).
            return True
        # Если элемент появился до истечения времени, возвращаем False.
        return False

    def is_disappeared(self, how, what, timeout=4): # проверяет, исчез ли элемент со страницы
        try:
            # Ожидаем исчезновения элемента с заданным локатором.
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            # Если по истечении времени элемент все еще присутствует, возвращаем False.
            return False
        # Если элемент исчез, возвращаем True.
        return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    #
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"


    def guest_clik_button_see_basket(self):  # просмотреть корзину
        link = self.browser.find_element(*BasePageLocators.CART)
        link.click()