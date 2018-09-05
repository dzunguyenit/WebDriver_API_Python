from WebDriver_API.abstractPage import commonFunction

common = commonFunction()
common.openurl("http://daominhdam.890m.com/")
common.hoverMouse("//button[contains(text(),'Click for JS Alert')]")
common.clickToElement("//button[contains(text(),'Click for JS Alert')]")
common.switchToAlert()
assert "I am a JS Alert" in common.getTextAlert()
common.acceptAlert()
assert "You clicked an alert successfully" in common.getTextElement("//p[@id='result']")
common.quitBrowser()
