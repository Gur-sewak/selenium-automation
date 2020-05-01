import os
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome("C:\\Users\\acer\\PycharmProjects\\selenium-automation\\driver\\chromedriver.exe")

#1
driver.get("http://msn.com")

#2
driver.find_element_by_tag_name('body').send_keys(Keys.LEFT_CONTROL+ "T")
driver.switch_to.window(driver.window_handles[-1])
driver.get("http://cnn.com")

#3
driver.find_element_by_tag_name('body').send_keys(Keys.LEFT_CONTROL+ 't')
driver.switch_to.window(driver.window_handles[-1])