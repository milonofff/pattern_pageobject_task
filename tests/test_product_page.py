import pytest
from pattern_pageobject_task.pages.product_page import ProductPage

# head = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
# links = [f"{head}{num}" for num in range(10)]
# links[7] = pytest.param(links[7], marks=pytest.mark.xfail)
# @pytest.mark.parametrize('link', links)
# def test_guest_can_add_product_to_basket(browser, link): # Этот тест проверяет добавляется ли продукт в корзину.
#     product_page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
#     product_page.open()  # открываем страницу, вызываем метод open() из BasePage
#     product_page.delivering_basket() # Этот метод находит кнопку добавить в корзину и кликает по ней
#     product_page.solve_quiz_and_get_code() # Вводит расчетные значения в alert
#     product_page.should_be_message_about_adding_product() # Проверяет успешное добавление товара в корзину
#     product_page.should_be_message_about_total_price() # Проверяет успешное добавление цены товара в корзину


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): # Этот тест проверяет сообщение после добавления продукта в корзину.
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()  # открываем страницу, вызываем метод open() из BasePage
    product_page.delivering_basket()  # Этот метод находит кнопку добавить в корзину и кликает по ней
    product_page.solve_quiz_and_get_code()  # Вводит расчетные значения в alert
    product_page.should_not_be_success_message() # проверяет, что сообщение об успешной операции не присутствует на странице


def test_guest_cant_see_success_message(browser):# Этот тест проверяет сообщение до добавления продукта в корзину.
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()  # открываем страницу, вызываем метод open() из BasePage
    product_page.should_not_be_success_message()  # проверяет, что сообщение об успешной операции не присутствует на странице


def test_message_disappeared_after_adding_product_to_basket(browser):# Этот тест проверяет исчезло ли сообщение после добавления продукта в корзину.
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()  # открываем страницу, вызываем метод open() из BasePage
    product_page.delivering_basket()  # Этот метод находит кнопку добавить в корзину и кликает по ней
    product_page.solve_quiz_and_get_code()  # Вводит расчетные значения в alert
    product_page.should_be_success_message()  # Проверяем, что нет сообщения об успехе