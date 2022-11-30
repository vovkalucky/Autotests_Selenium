import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()

class TestAbs(unittest.TestCase):
    def test_registration1(self):
        browser.get(link1)
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']").send_keys('Vladimir')
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']").send_keys('Galin')
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']").send_keys('vov@bk.ru')
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", f"{welcome_text} not expected!")

    def test_registration2(self):
        browser.get(link2)
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your name']").send_keys('Vladimir')
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']").send_keys('Galin')
        browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']").send_keys('vov@bk.ru')
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", f"{welcome_text} not expected!")


if __name__ == "__main__":
    unittest.main()