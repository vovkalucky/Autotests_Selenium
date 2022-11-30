from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/alert_accept.html')
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
confirm = driver.switch_to.alert
confirm.accept()
x = int(driver.find_element(By.CSS_SELECTOR, '#input_value').text)
y = calc(x)
driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
