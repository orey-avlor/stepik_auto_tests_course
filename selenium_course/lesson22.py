from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def summ(x, y):
	return str(int(x) + int(y))


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.ID, "num1")
    x1 = x.text
    y = browser.find_element(By.ID, "num2")
    y1 = y.text
    z = summ(x1, y1)
    browser.find_element(By.ID, "dropdown").click()
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(z)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
