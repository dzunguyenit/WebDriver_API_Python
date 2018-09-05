from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")


class commonFunction:

    def openurl(self, url):
        driver.get(url)
        driver.maximize_window()

    def backToPage(self):
        driver.back()

    def forwardToPage(self):
        driver.forward()

    def refreshPage(self):
        driver.refresh()

    def getTitle(self):
        return driver.title

    def getCurrentUrl(self):
        return driver.current_url

    def clickToElement(self, locator):
        driver.find_element_by_xpath(locator).click()

    def quitBrowser(self):
        driver.quit()

    def sendKeysToElement(self, locator, value):
        driver.find_element_by_xpath(locator).clear()
        driver.find_element_by_xpath(locator).send_keys(value)

    def uploadFile(self, locator, value):
        driver.find_element_by_xpath(locator).send_keys(value)

    def getTextElement(self, locator):
        return driver.find_element_by_xpath(locator).text

    def selectItemInDropdown(self, locator, value):
        dropdown = Select(driver.find_element_by_xpath(locator))
        dropdown.select_by_visible_text(value)

    def getAtribute(self, locator):
        return driver.find_element_by_xpath(locator).get_attribute()

    def acceptAlert(self):
        alert = driver.switch_to.alert
        alert.accept()

    def switchToAlert(self):
        driver.switch_to.alert

    def cancelAlert(self):
        alert = driver.switch_to.alert
        alert.dismiss()

    def getTextAlert(self):
        alert = driver.switch_to.alert
        return alert.text

    def sendKeyAlert(self, value):
        alert = driver.switch_to.alert
        alert.send_keys(value)

    def switchWindowByTitle(self, value):
        allWindow = driver.window_handles
        for handle in allWindow:
            driver.switch_to.window(handle)
            titleWindow = driver.title
            if titleWindow == value:
                break

    def getWindowParentID(self):
        return driver.current_window_handle

    def switchToIframe(self, locator):
        iframeLabel = driver.find_element_by_xpath(locator)
        driver.switch_to.frame(iframeLabel)

    def switchToDefaultContent(self):
        driver.switch_to.default_content()

    def hoverMouse(self, locator):
        element = driver.find_element_by_xpath(locator)
        action = ActionChains(driver)
        action.move_to_element(element).perform()

    def executeJavascriptToBrowser(self, value):
        driver.execute_script(value)

    def executeJavascriptToElement(self, locator):
        element = driver.find_element_by_xpath(locator)
        driver.execute_script("arguments[0].click();", element)

    def scrollToBottomPage(self):
        driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

    def scrollToElement(self, locator):
        element = driver.find_element_by_xpath(locator)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def highlightElement(self, locator):
        element = driver.find_element_by_xpath(locator)
        driver.execute_script("arguments[0].style.border='6px groove red'", element)

    def removeAttributeInDOM(self, locator, attribute):
        element = driver.find_element_by_xpath(locator)
        driver.execute_script("arguments[0].removeAttribute('" + attribute + "');", element)

    def waitForControlVisible(self, locator):
        wait = WebDriverWait(driver, 30)
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, locator)))
