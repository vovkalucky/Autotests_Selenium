from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, 'div.first_block &gt; div.form-group.first_class &gt; input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'div.first_block &gt; div.form-group.second_class &gt; input')
    input2.send_keys('Fomin')
    input3 = browser.find_element(By.CSS_SELECTOR, 'div.first_block &gt; div.form-group.third_class &gt; input')
    input3.send_keys('mail@mail.ru')
    #Заполнение не обязательных полей
    #input4 = browser.find_element(By.CSS_SELECTOR, 'div.second_block &gt; div.form-group.first_class &gt; input')
    #input4.send_keys('+79297222222')
    #input5 = browser.find_element(By.CSS_SELECTOR, 'div.second_block &gt; div.form-group.second_class &gt; input')
    #input5.send_keys('Andres')
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()