import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    # Открыть страницу http://suninjuly.github.io/get_attribute.html
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Считать значение для переменной x.
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    # Посчитать математическую функцию от x.
    y = calc(x)
    # Ввести ответ в текстовое поле.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    # Отметить checkbox "I'm the robot".
    input2 = browser.find_element(By.XPATH, '//*[@id="robotCheckbox"]')
    input2.click()
    # Выбрать radiobutton "Robots rule!".
    input3 = browser.find_element(By.CSS_SELECTOR, '[value="robots"]')
    input3.click()
    # Нажать на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
