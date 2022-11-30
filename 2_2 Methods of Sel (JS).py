import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/execute_script.html")
x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
y = calc(x)

radiobutton_element = driver.find_element(By.CSS_SELECTOR, "#robotsRule")
driver.execute_script("return arguments[0].scrollIntoView(true);", radiobutton_element)
radiobutton_element.click()

driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
#driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
submit_element = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
driver.execute_script("return arguments[0].scrollIntoView(true);", submit_element)

submit_element.click()