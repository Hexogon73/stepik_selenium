"""Плагины и перезапуск тестов
будем перезапускать упавший тест, чтобы еще раз убедиться, что он действительно нашел баг, а не упал случайно.Для этого мы будем использовать плагин pytest-rerunfailures
pip install pytest-rerunfailures==3.1
Чтобы указать количество перезапусков для каждого из упавших тестов, нужно добавить в командную строку параметр:

"--reruns n", где n - это количество перезапусков
Дополнительно мы указали параметр "--tb=line", чтобы сократить лог с результатами теста
pytest -v --tb=line --reruns 1 --browser_name=chrome Lesson_3/3_6_pytest_parametrize/test_rerun.py

pytest==3.10.1
pytest-rerunfailures==3.1
"""

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")


def test_guest_should_see_login_link_fail(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#magic_link")
