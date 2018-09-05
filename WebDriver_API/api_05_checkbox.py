from WebDriver_API.abstractPage import commonFunction
common = commonFunction()
common.openurl("http://demos.telerik.com/kendo-ui/styling/checkboxes")
common.executeJavascriptToElement("//label[text()='Dual-zone air conditioning']/preceding-sibling::input")
common.quitBrowser()

