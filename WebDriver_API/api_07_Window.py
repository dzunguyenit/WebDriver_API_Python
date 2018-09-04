from selenium import webdriver

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://daominhdam.890m.com/")
driver.maximize_window()

parentWindow = driver.current_window_handle
driver.find_element_by_xpath("//a[contains(text(),'Click Here')]").click()
allWindow = driver.window_handles

for handle in allWindow:
    driver.switch_to.window(handle)
    titleWindow = driver.title
    if titleWindow == "Google":
        break
print(driver.title)
assert "Google" in driver.title
driver.switch_to.window(parentWindow)
print(driver.title)
assert "SELENIUM WEBDRIVER FORM DEMO" in driver.title
driver.quit()
