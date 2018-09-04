import random

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://daominhdam.890m.com/")
driver.maximize_window()

driver.find_element_by_xpath("//button[@id='button-enabled']").click()
assert "http://daominhdam.890m.com/#" in driver.current_url
driver.back()
elementButton = driver.find_element_by_xpath("//button[text()='Click for JS Alert']")
driver.execute_script("$('button:contains(\"Click for JS Alert\")').click();")
driver.quit()
