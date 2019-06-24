from selenium import webdriver
import math

link = "http://SunInJuly.github.io/execute_script.html"
d = webdriver.Chrome()
d.get(link)

text = math.log(math.fabs(12*math.sin(int(d.find_element_by_id("input_value").text))))

d.execute_script("window.scrollBy(0,100)")
d.find_element_by_id("answer").send_keys(str(text))
d.find_element_by_id("robotCheckbox").click()
d.find_element_by_css_selector("[for='robotsRule']").click()
d.find_element_by_class_name("btn").click()