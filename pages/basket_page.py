from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

    def should_be_empty_cart_message(self):
        """Ожидаем, что корзина пуста, и отображается текст 'Ваша корзина пуста'"""
        self.browser.save_screenshot(r"D:\Python\pyQA\pattern_pageobject_task\logs\screenshot1.png")
        empty_cart_message = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(BasketPageLocators.CART_IS_EMPTY))
        assert "Ваша корзина пуста" in empty_cart_message.text, "Ожидался текст о пустой корзине, но его нет"


    def should_be_items_in_cart_message(self):
        self.browser.save_screenshot(r"D:\Python\pyQA\pattern_pageobject_task\logs\screenshot2.png")
        items_in_cart_message = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(BasketPageLocators.ITEMS_IN_CART))
        assert "Товары в корзине" in items_in_cart_message.text, "Ожидался текст о наличии товаров в корзине, но его нет"