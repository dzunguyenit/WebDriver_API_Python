from selenium import webdriver

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://www.helloselenium.com/2015/03/how-to-upload-file-using-sendkeys.html")
driver.maximize_window()

driver.find_element_by_xpath("//input[@name='uploadFileInput']").send_keys("C:\Ao.jpg")
driver.find_element_by_xpath("//input[@name='uploadFileButton']").click()
driver.quit()
