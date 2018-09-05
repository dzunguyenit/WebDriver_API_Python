from WebDriver_API.abstractPage import commonFunction

common = commonFunction()
common.openurl("http://the-internet.herokuapp.com/dynamic_loading/2")
common.clickToElement("//button[contains(text(),'Start')]")
common.waitForControlVisible("//h4[contains(text(),'Hello World!')]")
assert "Hello World!" in common.getTextElement("//h4[contains(text(),'Hello World!')]")
common.quitBrowser()

