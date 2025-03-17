from selenium.common.exceptions import NoSuchElementException


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