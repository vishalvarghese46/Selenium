from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox(executable_path="C:\\Users\\Optimised\\Downloads\\geckodriver.exe")
driver.maximize_window()

driver.get("https://www.wikipedia.org/")

#driver.find_element_by_id("searchLanguage").click()

dropdown = Select(driver.find_element_by_id("searchLanguage"))
dropdown.select_by_value("ca")

