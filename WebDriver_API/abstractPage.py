from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://demo.guru99.com/v4/")
driver.maximize_window()
urlHomeBank = driver.current_url

randomEmail = "vu" + "@gmail.com"
#+ str(random.randint(1,99999999))

driver.find_element_by_xpath("//a[contains(text(),'here')]").click()
driver.find_element_by_xpath("//input[@name='emailid']").send_keys(randomEmail)

# assert "Python1" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.quit()