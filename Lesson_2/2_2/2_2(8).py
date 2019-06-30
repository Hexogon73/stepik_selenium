import os

from selenium import webdriver

"""Задание: загрузка файла

Открыть страницу http://suninjuly.github.io/file_input.html
Заполнить текстовые поля: имя, фамилия, email
Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
Нажать кнопку "Отправить"
"""

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/file_input.html')

firstname_input = browser.find_element_by_css_selector('input[name="firstname"]')
lastname_input = browser.find_element_by_css_selector('input[name="lastname"]')
email_input = browser.find_element_by_css_selector('input[name="email"]')

firstname_input.send_keys("firstname_TEST")
lastname_input.send_keys("lastname_TEST")
email_input.send_keys("email@mail.ru")

current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, '2_2(8).txt')  # добавляем к этому пути имя файла
print(file_path)
file_input = browser.find_element_by_css_selector('input[name="file"]')
file_input.send_keys(file_path)
browser.find_element_by_css_selector('button[type="submit"]').click()

# дополнительно
print(os.path.abspath(__file__))                   # полный путь к исполняемому файлу
print(os.path.abspath(os.path.dirname(__file__)))  # на уровень выше относительно исполняемого файла
