from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://demos.telerik.com/kendo-ui/dragdrop/angular")
driver.maximize_window()

dragFrom = driver.find_element_by_xpath("//div[@id='draggable']")
target = driver.find_element_by_xpath("//div[@id='droptarget']")
action = ActionChains(driver)
action.drag_and_drop(dragFrom, target).perform()
assert "You did great!" in target.text
driver.quit()
