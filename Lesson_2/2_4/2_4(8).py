"""Задание: ждем нужный текст на странице
Попробуем теперь написать программу, которая будет бронировать нам дом для отдыха по строго заданной цене.
Более высокая цена нас не устраивает, а по более низкой цене объект успеет забронировать кто-то другой.

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/explicit_wait2.html
Дождаться, когда цена дома уменьшится до 10000 RUR (ожидание нужно установить не меньше 12 секунд)
Нажать на кнопку "Забронировать"
Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение
Чтобы определить момент, когда стоимость дома уменьшится до 10000 RUR, используйте метод text_to_be_present_in_element
 из библиотеки expected_conditions.
"""
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

browser = webdriver.Chrome()


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


browser.get('http://suninjuly.github.io/explicit_wait2.html')

WebDriverWait(browser, 12).until(
    expected_conditions.text_to_be_present_in_element((By.ID, 'price'), '10000 RUR'))
browser.find_element(By.CSS_SELECTOR, 'button[id="book"]').click()

x = int(browser.find_element_by_id('input_value').text)
answer_input = browser.find_element_by_id('answer').send_keys(calc(x))
browser.find_element_by_css_selector('button[type="submit"]').click()
