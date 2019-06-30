# -*- coding: utf-8 -*-
import math

from selenium import webdriver


"""Задание на execute_script

Открыть страницу http://SunInJuly.github.io/execute_script.html.
Считать значение для переменной x.
Посчитать математическую функцию от x.
Проскроллить страницу вниз.
Ввести ответ в текстовое поле.
Выбрать checkbox "Подтверждаю, что являюсь роботом".
Переключить radiobutton "Роботы рулят!".
Нажать на кнопку "Отправить".
"""

browser = webdriver.Chrome()


def calc(value):
    return str(math.log(abs(12 * math.sin(int(value)))))


link = 'http://SunInJuly.github.io/execute_script.html'
browser.get(link)
x = int(browser.find_element_by_id('input_value').text)
answer = calc(x)

answer_input = browser.find_element_by_id('answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", answer_input)
answer_input.send_keys(calc(x))
robot_checkbox = browser.find_element_by_id('robotCheckbox').click()
robots_rule_radio = browser.find_element_by_id('robotsRule').click()
browser.find_element_by_css_selector('button[type="submit"]').click()
