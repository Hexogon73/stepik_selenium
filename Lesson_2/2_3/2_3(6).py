"""Задание: переход на новую вкладку

В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить WebDriver
на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
"""

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/redirect_accept.html'
browser.get(link)

time.sleep(1)
browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
new_window = browser.window_handles[1]  # получаем имя новой вкладки
browser.switch_to.window(new_window)  # переключаемся на новую вкладку
x = int(browser.find_element_by_id('input_value').text)
answer_input = browser.find_element_by_id('answer').send_keys(calc(x))
browser.find_element_by_css_selector('button[type="submit"]').click()

# bonus: return into first window
first_window = browser.window_handles[0]  # получаем имя новой вкладки
browser.switch_to.window(first_window)  # переключаемся на новую вкладку
