import pytest
from pattern_pageobject_task.pages.login_page import LoginPage
from pattern_pageobject_task.pages.main_page import MainPage
from pattern_pageobject_task.pages.basket_page import BasketPage


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):  # тест проверяет переход на страницу логина с главной страницы.
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу, вызываем метод open() из BasePage
        page.go_to_login_page()  # Этот метод находит кнопку или ссылку "Войти" и кликает по ней
        login_page = LoginPage(browser, browser.current_url)  # создаем объект LOGINPAGE, передавая веб-драйвер, текущий URL
        login_page.should_be_login_page()  # проверяет наличие ссылки на логин

    def test_guest_should_see_login_link(self, browser):  # тест проверяет, отображается ли ссылка "Войти" на главной странице.
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.should_be_login_link()


@pytest.mark.old
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser): # Корзина по умолчанию должна быть пуста, если пользователь не добавлял туда товары
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.guest_clik_button_see_basket()  # нажимаем на кнопку корзина
    page.should_be_empty_cart_message()  # ожидаем отсутсвия товаров в корзине

