from selenium import webdriver
import time
import json
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\Optimised\\Downloads\\chromedriver.exe")

driver.get("https://nweather.futuredecisions.net")

driver.find_element_by_name('email').send_keys('peterreeves@optimisedbuildings.com')
driver.find_element_by_name('password').send_keys('Optimised1234!')
driver.find_element_by_tag_name("button").click()

#file = json.load("daveWeather.json")
#for location in file:
time.sleep(6)

driver.find_element_by_xpath('/html/body/app-root/app-topnavigationlayout/div/div/app-client-keys/div/div/div[2]/div/app-ibox/div/div[2]/div/div[1]/div[2]/a').click()

driver.find_element_by_xpath('//input[@ng-reflect-placeholder="Friendly name"]').send_keys('Vishal')
driver.find_element_by_xpath('//input[@ng-reflect-placeholder="Notes"]').send_keys('Success')
driver.find_element_by_xpath('//input[@ng-reflect-placeholder="Weather Location"]').send_keys('Morrisons Coalville')
driver.find_element_by_xpath('//input[@ng-reflect-placeholder="Weather Location"]').send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element_by_xpath('/html/body/app-root/app-topnavigationlayout/div/div/app-client-keys-create/div/div/div/form/app-ibox/div/div[2]/div/div[4]/div[2]/button').click()
time.sleep(5)
driver.find_element_by_class_name('swal-button-container').click()