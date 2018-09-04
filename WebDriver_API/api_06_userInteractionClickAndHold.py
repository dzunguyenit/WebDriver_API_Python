from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://jqueryui.com/resources/demos/selectable/display-grid.html")
driver.maximize_window()

listElement = driver.find_elements_by_xpath("//ol[@id='selectable']/li")
action = ActionChains(driver)
action.click_and_hold(listElement[0]).click_and_hold(listElement[3]).click().perform()
action.release()

driver.quit()
