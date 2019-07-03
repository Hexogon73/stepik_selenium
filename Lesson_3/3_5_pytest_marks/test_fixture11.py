import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

"""start run:
pytest -s -v -rsx test_fixture11.py
* -rxs - required to show the reason for xfailed text
"""


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1(object):
    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
