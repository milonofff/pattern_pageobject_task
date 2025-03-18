from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, "//*[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//*[@id='register_form']")

class ProductPageLocators():
    ADD_CART = (By.XPATH, "//*[@id='add_to_basket_form']/button")
    #SUCCESS_MESSAGE = (By.XPATH, "")