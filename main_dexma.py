from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\Optimised\\Downloads\\chromedriver.exe")
driver.maximize_window()

driver.get("https://optimisedbuildings.dexcell.com/login.htm;jsessionid=5A7EF74AE91DEB63E33C1A37C5856DD8")


username = driver.find_element_by_name('j_username')
username.send_keys('vishal@optimisedbuildings.com')

password = driver.find_element_by_name('j_password')
password.send_keys('achanteandixxxx')

button = driver.find_element_by_class_name('btn')
#time.sleep(5)
button.send_keys(Keys.ENTER)

time.sleep(5)
elem = driver.find_element_by_link_text('3786 - Morrisons')
elem
#time.sleep(5)

elem = driver.find_element_by_id('analysis_section')
elem.click()














elem2 = driver.find_element_by_id('evolution')
elem2.click()

time.sleep(10)

your_choice = driver.find_element_by_xpath("//select/option[@value='433191']")
time.sleep(20)
your_choice.click()



# #driver.quit()
