from selenium import webdriver
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://www.myntra.com/")
driver.maximize_window()

infoPersional = driver.find_element_by_xpath("//div[@class='desktop-userIconsContainer']")
action = ActionChains(driver)
action.move_to_element(infoPersional).perform()

btnlogin = driver.find_element_by_xpath("//a[contains(text(),'login')]")
action = ActionChains(driver)
action.move_to_element(btnlogin).click().perform()

driver.quit()
