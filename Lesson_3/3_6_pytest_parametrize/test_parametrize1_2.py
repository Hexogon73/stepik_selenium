import pytest
from selenium import webdriver

"""
PyTest позволяет запустить один и тот же тест с разными входными параметрами.
Для этого используется декоратор @pytest.mark.parametrize().
В @pytest.mark.parametrize() нужно передать параметр, который должен изменяться, и список значений параметра.
В самом тесте наш параметр тоже нужно передавать в качестве аргумента.
Обратите внимание, что внутри декоратора имя параметра оборачивается в кавычки, а в списке аргументов теста
кавычки не нужны

pytest -s -v Lesson_3/3_6_pytest_parametrize/test_parametrize1_2.py
"""


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('language', ["ru", "en-gb"])
class TestLogin(object):
    def test_guest_should_see_login_link(self, browser, language):
        link = "http://selenium1py.pythonanywhere.com/{}/".format(language)
        browser.get(link)
        browser.find_element_by_css_selector('#login_link')
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, browser, language):
        link = "http://selenium1py.pythonanywhere.com/{}/".format(language)
        browser.get(link)
        browser.find_element_by_css_selector('div[class^="navbar primary"]')
        # этот тест тоже запустится дважды
