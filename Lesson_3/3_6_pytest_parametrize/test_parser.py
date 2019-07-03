link = "http://selenium1py.pythonanywhere.com/"

"""pytest Lesson_3/3_6_pytest_parametrize/test_parser.py
pytest -s -v --browser_name=chrome Lesson_3/3_6_pytest_parametrize/test_parser.py
pytest -s -v --browser_name=firefox Lesson_3/3_6_pytest_parametrize/test_parser.py
pytest -s -v --browser_name=c Lesson_3/3_6_pytest_parametrize/test_parser.py
pytest -s -v --browser_name=f Lesson_3/3_6_pytest_parametrize/test_parser.py

pytest -s -v --browser_name=c --language=en Lesson_3/3_6_pytest_parametrize/test_parser.py
pytest -s -v --browser_name=f --language=en Lesson_3/3_6_pytest_parametrize/test_parser.py
"""


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")
