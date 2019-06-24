from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration2.html"
driver = webdriver.Chrome()
driver.get(link)

name = driver.find_element_by_css_selector("div.first_block .first")
name.send_keys("Ivan")
surname = driver.find_element_by_css_selector("div.first_block .second")
surname.send_keys("Petrov")
mail = driver.find_element_by_css_selector("div.first_block .third")
mail.send_keys("mail@mail.ru")

button = driver.find_element_by_class_name("btn")
button.click()

time.sleep(1)

welcomeText = driver.find_element_by_tag_name("h1")
text = welcomeText.text

assert "Поздравляем! Вы успешно зарегистировались!" == text