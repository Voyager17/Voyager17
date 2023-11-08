import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)


try:
    # Fill fields
    browser.find_element(By.NAME, "firstname").send_keys("Evgenii")
    browser.find_element(By.NAME, "lastname").send_keys("Timofeev")
    browser.find_element(By.NAME, "email").send_keys("ugabuga@yandex.ru")

    current_dir = os.path.abspath(
        os.path.dirname(__file__)
    )  # получаем путь к папке скрипта
    file_path = os.path.join(current_dir, "text.txt")  # путь к текстовому файлу
    browser.find_element(By.ID, "file").send_keys(file_path)

    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    time.sleep(30)
    browser.quit()
