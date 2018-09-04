from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://daominhdam.890m.com/")
driver.maximize_window()

elementTooltip = driver.find_element_by_xpath("//button[contains(text(),'Click for JS Alert')]")
action = ActionChains(driver)
action.move_to_element(elementTooltip).perform()
elementTooltip.click()
alert = driver.switch_to.alert
assert "I am a JS Alert" in alert.text
alert.accept()
textResult = driver.find_element_by_xpath("//p[@id='result']").text
assert "You clicked an alert successfully" in textResult
driver.quit()
