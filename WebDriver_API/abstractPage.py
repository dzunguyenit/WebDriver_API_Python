from selenium import webdriver

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")


class commonFunction:
    def openurl(self, url):
        driver.get(url)
        driver.maximize_window()

    def click(self, locator):
        driver.find_element_by_xpath(locator).click()

    def quitBrowser(self):
        driver.quit()

    def sendKeysToElement(self, locator, value):
        driver.find_element_by_xpath(locator).send_keys(value)
