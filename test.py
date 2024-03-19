import math
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('https://suninjuly.github.io/explicit_wait2.html')

    price_is_100 = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    btn1 = browser.find_element(By.CLASS_NAME, 'btn')
    btn1.click()


    x_element = browser.find_element(By.CSS_SELECTOR, '.form-group label #input_value')
    x = x_element.text
    y = calc(x)

    i = browser.find_element(By.TAG_NAME, 'input')
    i.send_keys(y)

    btn = browser.find_element(By.ID, 'solve')
    btn.click()
finally:
    browser.quit()
