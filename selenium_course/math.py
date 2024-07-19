import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/find_link_text"
text_link = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.LINK_TEXT, text_link)
    input1.click()
    input2 = browser.find_element(By.NAME, "first_name")
    input2.send_keys("Ivan")
    input3 = browser.find_element(By.NAME, "last_name")
    input3.send_keys("Petrov")
    input4 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div:nth-child(3) > input")
    input4.send_keys("Smolensk")
    input5 = browser.find_element(By.ID, "country")
    input5.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
