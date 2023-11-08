import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "https://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Find element
    number_1 = int(browser.find_element(By.ID, "num1").text)
    number_2 = int(browser.find_element(By.ID, "num2").text)
    total = number_2 + number_1

    select_list = Select(browser.find_element(By.ID, "dropdown"))
    select_list.select_by_value(str(total))
    # Fill the text field
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
