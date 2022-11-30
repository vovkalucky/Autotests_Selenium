import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/selects2.html")

sum = int(driver.find_element(By.ID, "num1").text) + int(driver.find_element(By.ID, "num2").text)

print(sum)
select_element = driver.find_element(By.CSS_SELECTOR, "select").click()
driver.find_element(By.CSS_SELECTOR, f"[value='{sum}']").click()

driver.execute_script("alert('Robots at work');")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()

