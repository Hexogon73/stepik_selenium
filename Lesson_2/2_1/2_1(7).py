# -*- coding: utf-8 -*-
import math

from selenium import webdriver

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = 'http://suninjuly.github.io/get_attribute.html'
browser.get(link)
treasure = browser.find_element_by_id('treasure')
x = treasure.get_attribute('valuex')
answer = browser.find_element_by_id('answer').send_keys(calc(x))
robot_checkbox = browser.find_element_by_id('robotCheckbox').click()
robots_rule_radio = browser.find_element_by_id('robotsRule').click()
browser.find_element_by_id('robotsRule').click()
browser.find_element_by_css_selector('button[type="submit"]').click()
