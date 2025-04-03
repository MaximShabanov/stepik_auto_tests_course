from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x, y):
  return int(x) + int(y)

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "#num1").text
    y = browser.find_element(By.CSS_SELECTOR, "#num2").text

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(calc(x, y)))  # ищем элемент с текстом "Python"

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()