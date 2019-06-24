from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

opt = webdriver.ChromeOptions()
opt.add_experimental_option('w3c', False)
d = webdriver.Chrome(chrome_options=opt)

d.get("http://suninjuly.github.io/explicit_wait2.html")


price = WebDriverWait(d, 12).until(  #wait = WebDriverWait(d,12) | wait.until(...)
    EC.text_to_be_present_in_element((By.ID, 'price'), '10000 RUR')
)
d.find_element_by_css_selector('#book').click()
print(d.find_element_by_css_selector('#book').get_attribute('class'))

d.find_element_by_css_selector("#answer").send_keys(str(math.log(math.fabs(12*math.sin(int(d.find_element_by_id("input_value").text))))))
d.find_element_by_css_selector("#solve").click()