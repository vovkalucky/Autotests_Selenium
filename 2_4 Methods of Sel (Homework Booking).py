from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")
# говорим Selenium проверять в течение 12 секунд, пока цена не станет 100$
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
browser.find_element(By.CSS_SELECTOR, "#book").click()

x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
y = calc(x)

browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
browser.find_element(By.CSS_SELECTOR, "#solve").click()


