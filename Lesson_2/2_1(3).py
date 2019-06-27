# -*- coding: utf-8 -*-
import math
import time
from selenium import webdriver

browser = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/math.html"
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector('span[id = "input_value"]')
    x = x_element.text
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(y)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button[type="submit"]').click()
finally:
    time.sleep(5)
    browser.quit()
