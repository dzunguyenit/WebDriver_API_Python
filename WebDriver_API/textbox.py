import random

from selenium import webdriver

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://demo.guru99.com/v4/")
driver.maximize_window()
urlHomeBank = driver.current_url

randomNumber = random.randint(1, 99999999)
randomString = str(randomNumber)

randomEmail = "vu" + randomString + "@gmail.com"
customerName = "AUTOMATION TESTING"
dateOfBirth = "01/01/1989"
address = "PO Box 911 8331 Duis Avenue"
city = "Tampa"
state = "FL"
PIN = "466250"
mobileNumber = "4555442476"
passwordCustomer = "automation"

driver.find_element_by_xpath("//a[contains(text(),'here')]").click()
driver.find_element_by_xpath("//input[@name='emailid']").send_keys(randomEmail)
driver.find_element_by_xpath("//input[@name='btnLogin']").click()

userName = driver.find_element_by_xpath("//*[contains(text(),'User ID :')]/following-sibling::td").text
password = driver.find_element_by_xpath("//*[contains(text(),'Password :')]/following-sibling::td").text

driver.get(urlHomeBank)
driver.find_element_by_xpath("//input[@name='uid']").send_keys(userName)
driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
driver.find_element_by_xpath("//input[@name='btnLogin']").click()

driver.find_element_by_xpath("//a[contains(text(),'New Customer')]").click()
driver.find_element_by_xpath("//input[@name='name']").send_keys(customerName)
driver.find_element_by_xpath("//input[@name='dob']").send_keys(dateOfBirth)
driver.find_element_by_xpath("//textarea[contains(@name,'addr')]").send_keys(address)
driver.find_element_by_xpath("//input[@name='city']").send_keys(city)
driver.find_element_by_xpath("//input[@name='state']").send_keys(state)
driver.find_element_by_xpath("//input[@name='pinno']").send_keys(PIN)
driver.find_element_by_xpath("//input[@name='telephoneno']").send_keys(mobileNumber)
driver.find_element_by_xpath("//input[@name='emailid']").send_keys(randomEmail)
driver.find_element_by_xpath("//input[@name='password']").send_keys(passwordCustomer)
driver.find_element_by_xpath("//input[@name='sub']").click()

registerSuccessMsg = driver.find_element_by_xpath("//p[contains(text(),'Customer Registered Successfully!!!')]").text

assert "Customer Registered Successfully!!!" in registerSuccessMsg

# time.sleep(3000)

# assert "Python1" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.quit()
