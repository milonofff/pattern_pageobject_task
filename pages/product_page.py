import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):


    def delivering_basket(self):
        add_order = self.browser.find_element(*ProductPageLocators.ADD_CART)
        add_order.click()

    def get_product_name(self):
        return self.is_element_present(*ProductPageLocators.PRODUCT_NAME)
    def get_product_price(self):
        return self.is_element_present(*ProductPageLocators.PRODUCT_PRICE)

    def should_be_message_about_adding_product(self):
        # Сначала проверяем что элементы находятся на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_ADD), "Название товара отсутствует после добавления в корзину"
        # Текст элементов проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_add = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ADD).text
        assert product_name == message_add, f"Ожидалось '{product_name}', но получили '{message_add}'"

    def should_be_message_about_total_price(self):
        # Сначала проверяем что элементы находятся на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_CART), "Стоимость товара отсутствует после добавления в корзину"
        # Текст элементов проверки
        price_up_to = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        price_after = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CART).text
        assert price_up_to == price_after, f"Ожидалась цена '{price_up_to}', но получили '{price_after}'"

    def should_not_be_success_message(self): # проверяет, что сообщение об успешной операции не присутствует на странице
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_ADD), "Сообщение об успешном выполнении отображается, но его не должно быть"


    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME), "Сообщение об успешном выполнении отображается"