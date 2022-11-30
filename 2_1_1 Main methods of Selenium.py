from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/get_attribute.html")
img_element = driver.find_element(By.ID, "treasure")
x = img_element.get_attribute('valuex')
print(x)
y = calc(x)

input_element = driver.find_element(By.CSS_SELECTOR, "#answer")
input_element.send_keys(y)

checkbox_element = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox")
checkbox_element.click()

radiobutton_element = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
radiobutton_element.click()

submit_element = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
submit_element.click()