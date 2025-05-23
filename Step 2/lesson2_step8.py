from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    browser = webdriver.Chrome()
    link = "https://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
    input3.send_keys("Smolensk")

    element = browser.find_element(By.ID, "file")
    file_path = os.path.join("C:\\Users\\shabanovmy\\Downloads", "file.txt")
    element.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()