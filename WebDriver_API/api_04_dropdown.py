import random

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://daominhdam.890m.com/")
driver.maximize_window()

dropdown1 = Select(driver.find_element_by_xpath("//*[@id='job1']"))
dropdown1.select_by_visible_text("Automation Tester")
time.sleep(3)
dropdown1.select_by_value("manual")
time.sleep(3)
dropdown1.select_by_index(3)
time.sleep(3)

driver.quit()
