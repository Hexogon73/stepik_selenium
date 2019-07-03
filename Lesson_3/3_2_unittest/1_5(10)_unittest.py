# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class TestSuite(unittest.TestCase):
    def test_case1(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
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
        # находим элемент, содержащий текст
        welcome_text_elt = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual('Поздравляем! Вы успешно зарегистировались!', welcome_text, 'Auth Error')

    def test_case2(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
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
        # находим элемент, содержащий текст
        welcome_text_elt = WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual('Поздравляем! Вы успешно зарегистировались!', welcome_text, 'Auth Error')


if __name__ == "__main__":
    unittest.main()
