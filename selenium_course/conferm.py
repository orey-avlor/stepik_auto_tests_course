import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Открыть страницу https://suninjuly.github.io/math.html.
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button11 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button11.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    # Считать значение для переменной x.
    x_element = browser.find_element(By.CSS_SELECTOR, "span#input_value.nowrap")
    x = x_element.text
    # Посчитать математическую функцию от x.
    y = calc(x)
    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
