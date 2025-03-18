from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def delivering_basket(self):
        add_order = self.browser.find_element(*ProductPageLocators.ADD_CART)
        add_order.click()

    #def should_be_success_message(self):
        #assert self.is_element_present(*ProductPageLocators.ADD_CART), "Сообщение об успешном добавлении отсутствует!"
