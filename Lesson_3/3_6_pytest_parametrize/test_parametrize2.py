import math
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

"""https://stepik.org/lesson/237240/step/3

pytest -s -v Lesson_3/3_6_pytest_parametrize/test_parametrize2.py
"""


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


def get_answer():
    return str(math.log(int(time.time())))


class TestUFO(object):
    @pytest.mark.parametrize('link', links)
    def test_get_ufo_message(self, browser, link):
        browser.get(link)
        answer_input = WebDriverWait(browser, 20).until(
            expected_conditions.element_to_be_clickable(
                (By.CSS_SELECTOR, 'div[class="attempt"] textarea'))
        )
        answer_input.send_keys(get_answer())
        browser.find_element_by_css_selector('button[class^="submit"]').click()
        WebDriverWait(browser, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, '[class="attempt__message"]>span[class*="correct_icon"]'))
        )
        text_message = browser.find_element_by_css_selector('pre[class="smart-hints__hint"]').text
        assert text_message == 'Correct!', 'text_message({}) != "Correct!"'.format(text_message)
