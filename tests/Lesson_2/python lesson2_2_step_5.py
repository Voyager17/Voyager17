import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(value: str):
    return str(math.log(abs(12 * math.sin(int(value)))))


try:
    # Find element
    number_x = browser.find_element(By.ID, "input_value").text
    number_x = calc(number_x)

    # Scroll
    submit_button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    browser.execute_script("window.scrollBy(0, 100);")

    browser.find_element(By.ID, "answer").send_keys(number_x)

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()

    submit_button.click()
finally:
    time.sleep(30)
    browser.quit()
