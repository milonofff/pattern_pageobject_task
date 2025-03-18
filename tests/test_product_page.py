from pattern_pageobject_task.pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser): # Этот тест проверяет добавляется ли продукт в корзину.
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    product_page.open()  # открываем страницу, вызываем метод open() из BasePage
    product_page.delivering_basket() # Этот метод находит кнопку добавить в корзину и кликает по ней
    product_page.solve_quiz_and_get_code() # Вводит расчетные значения в alert
    #product_page.is_element_present() # Проверяет наличие alert