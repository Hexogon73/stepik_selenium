import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

"""start run:
pytest -s -v -m smoke test_fixture8.py
pytest -s -v -m "not smoke" test_fixture8.py
pytest -s -v -m "smoke or regression" test_fixture8.py
pytest -s -v -m "regression and win10" test_fixture8.py
pytest -s -v -m "smoke, regression" test_fixture8.py
"""


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1(object):

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    @pytest.mark.win10
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
