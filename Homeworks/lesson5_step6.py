from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://suninjuly.github.io/huge_form.html")

textFields = driver.find_elements_by_tag_name("input")

for field in textFields:
    field.send_keys("opa")

button = driver.find_element_by_css_selector("button.btn")
button.click()
