# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select

"""
Открыть страницу http://suninjuly.github.io/selects1.html
Посчитать сумму заданных чисел
Выбрать в выпадающем списке значение равное расчитанной сумме
Нажать кнопку "Отправить"
"""

browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/selects1.html'
browser.get(link)

num1 = int(browser.find_element_by_id('num1').text)
num2 = int(browser.find_element_by_id('num2').text)

answer = num1 + num2

select = Select(browser.find_element_by_class_name("custom-select"))
select.select_by_value(str(answer))

browser.find_element_by_css_selector('button[type="submit"]').click()
