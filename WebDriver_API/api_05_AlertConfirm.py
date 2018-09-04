from selenium import webdriver

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://daominhdam.890m.com/")
driver.maximize_window()

driver.find_element_by_xpath("//button[contains(text(),'Click for JS Confirm')]").click()
alert = driver.switch_to.alert
assert "I am a JS Confirm" in alert.text
alert.dismiss()
textResult = driver.find_element_by_xpath("//p[@id='result']").text
assert "You clicked: Cancel" in textResult
driver.quit()
