import pytest

from pattern_pageobject_task.pages.product_page import ProductPage


@pytest.mark.parametrize("product", ["the-shellcoders-handbook_209", "coders-at-work_207"])
def test_guest_can_add_product_to_basket(browser, product): # Этот тест проверяет добавляется ли продукт в корзину.
    link = f"http://selenium1py.pythonanywhere.com/ru/catalogue/{product}/?promo=newYear"
    product_page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()  # открываем страницу, вызываем метод open() из BasePage
    product_page.delivering_basket() # Этот метод находит кнопку добавить в корзину и кликает по ней
    product_page.solve_quiz_and_get_code() # Вводит расчетные значения в alert
    #product_page.is_element_present() # Проверяет наличие alert