from selenium import webdriver

link = "http://suninjuly.github.io/cats.html"
d = webdriver.Chrome()
d.get(link)
d.find_element_by_id("button")