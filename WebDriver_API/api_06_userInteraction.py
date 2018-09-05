from WebDriver_API.abstractPage import commonFunction

common = commonFunction()
common.openurl("http://www.myntra.com/")
common.hoverMouse("//div[@class='desktop-userIconsContainer']")
common.hoverMouse("//a[contains(text(),'login')]")
common.clickToElement("//a[contains(text(),'login')]")
common.quitBrowser()
