from selenium import webdriver
import math

link = "http://suninjuly.github.io/alert_accept.html"
d = webdriver.Chrome()
d.get(link)

d.find_element_by_css_selector(".btn").click()
d.switch_to.alert.accept()
d.find_element_by_css_selector("#answer").send_keys(str(math.log(math.fabs(12*math.sin(int(d.find_element_by_id("input_value").text))))))
d.find_element_by_css_selector(".btn").click()
