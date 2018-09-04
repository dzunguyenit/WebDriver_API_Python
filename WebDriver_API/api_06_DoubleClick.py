from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://www.seleniumlearn.com/double-click")
driver.maximize_window()

btnDouble = driver.find_element_by_xpath("//button[contains(text(),'Double-Click Me!')]")
action = ActionChains(driver)
action.double_click(btnDouble).perform()

driver.quit()
