"""Задание: принимаем alert
В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
"""
import math
from selenium import webdriver


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'
browser.get(link)

submit_button = browser.find_element_by_tag_name('button').click()
confirm = browser.switch_to.alert
confirm.accept()
x = int(browser.find_element_by_id('input_value').text)
answer_input = browser.find_element_by_id('answer').send_keys(calc(x))
browser.find_element_by_css_selector('button[type="submit"]').click()
