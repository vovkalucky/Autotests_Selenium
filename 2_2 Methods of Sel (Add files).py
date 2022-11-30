from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.get("http://suninjuly.github.io/file_input.html")
driver.find_element(By.CSS_SELECTOR, "[name = 'firstname']").send_keys('Vladimir')
driver.find_element(By.CSS_SELECTOR, "[name = 'lastname']").send_keys('Galkin')
driver.find_element(By.CSS_SELECTOR, "[name = 'email']").send_keys('vovq12@bk.ru')

#Прикрепляем файл
with open("file.txt", "w") as file:
  content = file.write("automationbypython")  # create test.txt file

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
driver.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)

driver.find_element(By.CSS_SELECTOR, "[type= 'submit']").click()

