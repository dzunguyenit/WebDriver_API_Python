from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

btnDouble = driver.find_element_by_xpath("//span[contains(text(),'right click me')]")
action = ActionChains(driver)
action.context_click(btnDouble).perform()

driver.quit()
