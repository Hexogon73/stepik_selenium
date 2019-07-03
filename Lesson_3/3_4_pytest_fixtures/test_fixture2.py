import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser() -> RemoteWebDriver:
    """Return WebDriver instance

    :return: WebDriver instance
    """
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1:
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser: RemoteWebDriver):
        """
        :param WebDriver browser: The browser's driver
        :return:
        """
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser: RemoteWebDriver):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
