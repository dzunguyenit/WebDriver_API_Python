from WebDriver_API.abstractPage import commonFunction
common = commonFunction()
common.openurl("http://daominhdam.890m.com/")
common.clickToElement("//button[@id='button-enabled']")
common.backToPage()
common.executeJavascriptToBrowser("$('button:contains(\"Click for JS Alert\")').click();")
common.quitBrowser()
