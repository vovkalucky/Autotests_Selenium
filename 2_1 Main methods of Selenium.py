# webdriver это и есть набор команд для управления браузером
from selenium import webdriver
# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("https://suninjuly.github.io/math.html")
x_element = driver.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
input_element = driver.find_element(By.CSS_SELECTOR, "#answer")
# Напишем текст ответа в найденное поле
input_element.send_keys(y)

checkbox_element = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
checkbox_element.click()

radiobutton_element = driver.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
radiobutton_element.click()

submit_element = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_element.click()


