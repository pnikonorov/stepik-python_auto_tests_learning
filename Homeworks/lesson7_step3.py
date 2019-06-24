from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
driver = webdriver.Chrome()
driver.get(link)

sum = int(driver.find_element_by_id("num1").text) + int(driver.find_element_by_id("num2").text)
select = Select(driver.find_element_by_id("dropdown"))
select.select_by_value(str(sum))
button = driver.find_element_by_class_name("btn").click()

