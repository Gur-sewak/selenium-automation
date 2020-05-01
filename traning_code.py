from selenium import webdriver
import time
import sys
from selenium.webdriver.common.keys import Keys

siteopening = webdriver.Chrome(
    "C:\\Users\\acer\\PycharmProjects\\selenium-automation\\driver\\chromedriver.exe")  # for chrome opening
siteopening.maximize_window()  # for maximimizing window

siteopening.get("https://www.flickr.com/")  # opening url
siteopening.find_element_by_name("text").send_keys("love YOU", Keys.ENTER)  # sending text to search
siteopening.execute_script("window.open('https://www.pixabay.com');")  # website open in new tab
siteopening.find_element_by_name("q").send_keys("love YOU", Keys.ENTER)
siteopening.execute_script("window.open('https://unsplash.com/');")  # website open in new tab
siteopening.find_element_by_name("searchKeyword").send_keys("love YOU", Keys.ENTER)
siteopening.execute_script("window.open('https://www.pexels.com/');")  # website open in new tab
siteopening.find_element_by_name("s").send_keys("love YOU", Keys.ENTER, )

time.sleep(100)  # wait for 100 sec
siteopening.quit()  # quiting browser
