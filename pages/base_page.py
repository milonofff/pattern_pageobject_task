from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
import math

"""
Создается базовый класс BasePage, 
от которого будут наследоваться 
другие Page Object классы.
"""
class BasePage():
    def __init__(self, browser, url, timeout=10):
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