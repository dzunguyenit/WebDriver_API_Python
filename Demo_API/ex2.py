from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")
driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("https://beecow.mediastep.ca/")
driver.maximize_window()
driver.find_element_by_xpath("//div[@class='modal-dialog']//a[@id='btn-start-mobi']").click()
time.sleep(4000)
driver.find_element_by_xpath("//a[@class='login']").click()
# time.sleep(4000)
# driver.find_element_by_xpath("//input[@id='usr']").send_keys("nguyenvuproduct@yopmail.com")
# driver.find_element_by_xpath("//fieldset//input[@id='pwd']").send_keys("123456")
# driver.find_element_by_xpath("//button[@class='btn-solid-orange btn-login']").click()
driver.quit()
