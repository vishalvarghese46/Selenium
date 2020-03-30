from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

driverPath = r'C:\Users\visha\Downloads'
driver = webdriver.Chrome(executable_path=f"{driverPath}\chromedriver.exe")
driver.maximize_window()
driver.get("https://optimisedbuildings.dexcell.com/login.htm;jsessionid=5A7EF74AE91DEB63E33C1A37C5856DD8")


username = driver.find_element_by_name('j_username')
username.send_keys('vishal@optimisedbuildings.com')

password = driver.find_element_by_name('j_password')
password.send_keys('Optimised1234')

button = driver.find_element_by_class_name('btn')
#time.sleep(5)
button.send_keys(Keys.ENTER)

time.sleep(5)
elem = driver.find_element_by_link_text('3786 - Morrisons')
elem.click()

driver.find_element_by_link_text('Settings').click()
driver.find_element_by_link_text('Gateways').click()
driver.find_element_by_id("new-gateway").click()
driver.find_element_by_xpath("//button[@data-type='weather']").click()
driver.find_element_by_id('next-button').click()



#driver.find_element_by_id('s2id_countryCode').click()
#driver.find_element_by_xpath("//option[@value='Albania']").click()
#driver.find_element_by_xpath("//select[@name='countryAndPostcode.countryCode']/option[text()='option_text']").click()
