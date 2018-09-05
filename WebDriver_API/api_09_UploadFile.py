from WebDriver_API.abstractPage import commonFunction

common = commonFunction()
common.openurl("http://www.helloselenium.com/2015/03/how-to-upload-file-using-sendkeys.html")
common.uploadFile("//input[@name='uploadFileInput']", "C:\Ao.jpg")
common.clickToElement("//input[@name='uploadFileButton']")
common.quitBrowser()
