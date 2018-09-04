from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://the-internet.herokuapp.com/dynamic_loading/2")
driver.maximize_window()

wait = WebDriverWait(driver, 30)
driver.find_element_by_xpath("//button[contains(text(),'Start')]").click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//h4[contains(text(),'Hello World!')]")))
textHello = driver.find_element_by_xpath("//h4[contains(text(),'Hello World!')]").text
assert "Hello World!" in textHello
driver.quit()
