# -*- coding: utf-8 -*-

from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

# Ваш код, который заполняет обязательные поля
first_name_input = browser.find_element_by_xpath('//label[text()="Имя*"]/parent::div/input')
first_name_input.send_keys('TestName')
second_name_input = browser.find_element_by_xpath('//label[text()="Фамилия*"]/parent::div/input')
second_name_input.send_keys('TestSecondName')
email_input = browser.find_element_by_xpath('//label[text()="Email*"]/parent::div/input')
email_input.send_keys('TestEmail')
# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
