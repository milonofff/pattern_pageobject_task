from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//*[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//*[@id='register_form']")

    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_CART = (By.XPATH, "//*[@id='add_to_basket_form']/button") # Кнопка добавить в корзину
    PRODUCT_NAME = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1") # Название товара до нажатия товара в корзину
    PRODUCT_PRICE = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]") # Стоимость товара до нажатия товара в корзину
    PRODUCT_NAME_ADD = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong") # Сообщение что товар добавлен в корзину  "//*[@id='messages']/div[1]/div/strong"
    PRODUCT_PRICE_CART = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong") # Сообщение что стоимость корзины теперь составляет
    DEFERRED_BENEFIT_OFFER = (By.XPATH, '//*[@id="messages"]/div[2]/div/strong') # Сообщение что ваша корзина удовлетворяет условиям предложения

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a') # Кнопка перехода в корзину
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    CART_IS_EMPTY = (By.XPATH, "//*[@id='content_inner']") # Корзина пуста
    ITEMS_IN_CART = (By.XPATH, "//*[@id='content_inner']/div[1]/div/h2") # Товары в корзине


