from selenium import webdriver

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://demos.telerik.com/kendo-ui/styling/radios")
driver.maximize_window()

radio = driver.find_element_by_xpath("//label[text()='2.0 Petrol, 147kW']/preceding-sibling::input")
driver.execute_script("arguments[0].click();", radio)
driver.quit()