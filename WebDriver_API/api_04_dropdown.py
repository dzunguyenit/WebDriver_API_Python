from WebDriver_API.abstractPage import commonFunction

common = commonFunction()
common.openurl("http://daominhdam.890m.com/")
common.selectItemInDropdown("//*[@id='job1']", "Automation Tester")
common.selectItemInDropdown("//*[@id='job1']", "Manual Tester")
common.quitBrowser()
