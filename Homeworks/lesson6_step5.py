from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
driver = webdriver.Chrome()
driver.get(link)

valueX = driver.find_element_by_id("treasure")
print(valueX.get_attribute("valuex"))
valueX = driver.find_element_by_id("treasure").get_attribute("valuex")
input1 = driver.find_element_by_id("answer")
input1.send_keys(calc(valueX))
btn = driver.find_element_by_class_name("btn")
print(btn.get_attribute("disabled"))

checkbox1 = driver.find_element_by_id("robotCheckbox")
print(checkbox1.get_attribute("checked"))
checkbox1.click()
print(checkbox1.get_attribute("checked"))

radiobutton1 = driver.find_element_by_id("robotsRule")
radiobutton1.click()
print(radiobutton1.get_attribute("checked"))

btn = driver.find_element_by_class_name("btn")

print(btn.get_attribute("disabled"))
btn.click()
