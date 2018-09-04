import random

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://demos.telerik.com/kendo-ui/styling/checkboxes")
driver.maximize_window()

checkbox = driver.find_element_by_xpath("//label[text()='Dual-zone air conditioning']/preceding-sibling::input")
driver.execute_script("arguments[0].click();", checkbox)
driver.quit()
