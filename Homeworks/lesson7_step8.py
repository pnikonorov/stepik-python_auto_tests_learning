from selenium import webdriver
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'txt.txt')

link = "http://suninjuly.github.io/file_input.html"
d = webdriver.Chrome()
d.get(link)

d.find_element_by_css_selector("[name='firstname']").send_keys("Ivan")
d.find_element_by_css_selector("[placeholder='Введите фамилию']").send_keys("Petrov")
d.find_element_by_css_selector("input[name='email']").send_keys("1@1.ru")
d.find_element_by_css_selector("input[id='file']").send_keys(file_path)
d.find_element_by_css_selector("button.btn").click()
