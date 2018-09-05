from WebDriver_API.abstractPage import commonFunction

abstract = commonFunction()
abstract.openurl("http://demo.guru99.com/v4/")
abstract.click("//a[contains(text(),'here')]")

abstract.sendKeysToElement("//input[@name='emailid']", "nguyenene")
abstract.quitBrowser()
