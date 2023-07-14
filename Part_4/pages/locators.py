from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

# class ProductPageLocators():
#     PROMO = "?promo=newYear"
#     #ADD_IN_BASKET = (By.TAG_NAME, "button[value='Добавить в корзину']")
#     ADD_IN_BASKET = (By.XPATH, '//button[@type="submit" and contains(@class, "btn btn-lg btn-primary btn-add-to-basket")]')

class ProductPageLocators(object):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")