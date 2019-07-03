link = "http://selenium1py.pythonanywhere.com/"

"""pytest Lesson_3/3_6_pytest_parametrize/test_conftest.py
"""


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
