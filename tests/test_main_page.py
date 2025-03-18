from pattern_pageobject_task.pages.login_page import LoginPage
from pattern_pageobject_task.pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser): # Этот тест проверяет переход на страницу логина с главной страницы.
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу, вызываем метод open() из BasePage
    page.go_to_login_page() # Этот метод находит кнопку или ссылку "Войти" и кликает по ней
    login_page = LoginPage(browser, browser.current_url)  # создаем объект LOGINPAGE, передавая веб-драйвер, текущий URL
    login_page.should_be_login_page() # проверяет наличие ссылки на логин
def test_guest_should_see_login_link(browser): # Этот тест проверяет, отображается ли ссылка "Войти" на главной странице.
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open() # открываем страницу
    page.should_be_login_link()


