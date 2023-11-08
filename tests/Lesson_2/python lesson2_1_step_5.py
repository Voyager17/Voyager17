import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)


def calc(value: str):
    return str(math.log(abs(12 * math.sin(int(value)))))


try:
    # Find element
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    # Fill the text field
    button = browser.find_element(By.CSS_SELECTOR, "#answer")
    button.send_keys(y)

    checkbox_button = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkbox_button.click()

    radio_button = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    radio_button.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()