import time

import pytest

from .base_page import BasePage
from .locators import ProductPageLocators
class ProductPage(BasePage):
    # def should_be_product_link(self):
    #     assert "handbook" in self.browser.current_url, "Title is not correct"
    #
    # def should_be_button_add(self):
    #     assert self.is_element_present(*ProductPageLocators.ADD_IN_BASKET), "Button is not presented"
    #     #assert self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET), "Button is not presented"
    #
    #
    # def add_in_basket(self):
    #     button_link = self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET)
    #     button_link.click()
    def press_button_add_to_basket(self):
        # Нажимаем кнопку Add to basket
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_message_about_adding(self):
        # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        # Затем получаем текст элементов для проверки
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        # Проверяем, что название товара присутствует в сообщении о добавлении
        # Это можно было бы сделать с помощью split() и сравнения строк,
        # Но не вижу необходимости усложнять код
        assert product_name in message, "No product name in the message"

    def should_be_message_basket_total(self):
         # Сначала проверяем, что элементы присутствуют на странице
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        # Затем получаем текст элементов для проверки
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Проверяем, что цена товара присутствует в сообщении со стоимостью корзины
        assert product_price in message_basket_total, "No product price in the message"

