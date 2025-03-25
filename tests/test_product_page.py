import time
import pytest
from pattern_pageobject_task.pages.product_page import ProductPage
from pattern_pageobject_task.pages.basket_page import BasketPage
from pattern_pageobject_task.pages.login_page import LoginPage

head = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
links = [f"{head}{num}" for num in range(10)]
links[7] = pytest.param(links[7], marks=pytest.mark.xfail)
@pytest.mark.need_review # Маркировка для пометки "нужно проверить"
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link): # тест проверяет добавляется ли продукт в корзину.
    product_page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()  # открываем страницу, вызываем метод open() из BasePage
    product_page.delivering_basket() # метод находит кнопку добавить в корзину и кликает по ней
    product_page.solve_quiz_and_get_code() # вводит расчетные значения в alert
    product_page.should_be_message_about_adding_product() # проверяет успешное добавление товара в корзину
    product_page.should_be_message_about_total_price() # проверяет успешное добавление цены товара в корзину


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): # тест проверяет сообщение после добавления продукта в корзину.
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()  # открываем страницу, вызываем метод open() из BasePage
    product_page.delivering_basket()  # Этот метод находит кнопку добавить в корзину и кликает по ней
    product_page.solve_quiz_and_get_code()  # Вводит расчетные значения в alert
    product_page.should_not_be_success_message() # проверяет, что сообщение об успешной операции не присутствует на странице


def test_guest_cant_see_success_message(browser):# тест проверяет сообщение до добавления продукта в корзину.
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()  # открываем страницу, вызываем метод open() из BasePage
    product_page.should_not_be_success_message()  # проверяет, что сообщение об успешной операции не присутствует на странице


def test_message_disappeared_after_adding_product_to_basket(browser):# тест проверяет исчезло ли сообщение после добавления продукта в корзину.
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    product_page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()  # открываем страницу, вызываем метод open() из BasePage
    product_page.delivering_basket()  # Этот метод находит кнопку добавить в корзину и кликает по ней
    product_page.solve_quiz_and_get_code()  # Вводит расчетные значения в alert
    product_page.should_be_success_message()  # Проверяем, что нет сообщения об успехе

def test_guest_should_see_login_link_on_product_page(browser): # проверяет наличие ссылки на вход на странице продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
@pytest.mark.need_review # Маркировка для пометки "нужно проверить"
def test_guest_can_go_to_login_page_from_product_page(browser): # проверяет, что гость может перейти на страницу входа со страницы продукта
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review # Маркировка для пометки "нужно проверить"
class TestUserAddToBasketFromProductPage():
    # Фикстура, которая будет запускаться перед каждым тестом
    pytest.fixture(scope="function", autouse=True)
    def setup(self, browser): # Регистрация и проверка нового пользователя
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        email = str(time.time()) + "@fakemail.org" # генерируем уникальный email на основе времени
        password = "Test12345!" # задаем пароль для регистрации
        page.register_new_user(email, password) # Регистрируем нового пользователя
        page.should_be_authorized_user() # Проверяем, что пользователь залогинен (отображается иконка пользователя)

    def test_user_cant_see_success_message(self, browser): # Проверяем сообщение об отсутствии товаров в корзине
        link = "http://selenium1py.pythonanywhere.com/catalogue/"
        page = BasketPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.guest_clik_button_see_basket() # нажимаем на кнопку корзина
        page.should_be_empty_cart_message() # Ожидаем отсутствия товаров в корзине

    @pytest.mark.skip
    def test_user_can_add_product_to_basket(self, browser):# Проверяем что товары присутсвуют в корзине
        link = "http://selenium1py.pythonanywhere.com/catalogue/"
        page = BasketPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.guest_clik_button_see_basket() # нажимаем на кнопку корзина
        page.should_be_items_in_cart_message() # Проверяем что в корзине есть товары

