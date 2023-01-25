from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

browser.get('https://www.yahoo.com/')
assert 'Yahoo' in browser.title 

time.sleep(5)
elem =  browser.find_element_by_name('p')  # Find the search box
elem.send_keys('seleniumhq' + Keys.RETURN)