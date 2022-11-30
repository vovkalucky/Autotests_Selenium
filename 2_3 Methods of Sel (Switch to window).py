from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/redirect_accept.html')
driver.find_element(By.CSS_SELECTOR,"[type='submit']").click()
# Чтобы узнать имя новой вкладки
new_window = driver.window_handles[1]
# Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти
driver.switch_to.window(new_window)
x = driver.find_element(By.CSS_SELECTOR, '#input_value').text
y = calc(x)
driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()



