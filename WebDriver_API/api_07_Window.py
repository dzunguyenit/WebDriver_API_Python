from WebDriver_API.abstractPage import commonFunction

common = commonFunction()
common.openurl("http://daominhdam.890m.com/")
parentWindow = common.getTitle()
common.clickToElement("//a[contains(text(),'Click Here')]")
common.switchWindowByTitle("Google")
assert "Google" in common.getTitle()
common.switchWindowByTitle(parentWindow)
assert "SELENIUM WEBDRIVER FORM DEMO" in common.getTitle()
common.quitBrowser()
