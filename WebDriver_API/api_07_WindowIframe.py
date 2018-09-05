from WebDriver_API.abstractPage import commonFunction

common = commonFunction()
common.openurl("http://www.hdfcbank.com/")

parentWindow = common.getTitle()
common.clickToElement("//a[@href='/htdocs/common/agri/index.html']")
common.switchWindowByTitle("HDFC Bank Kisan Dhan Vikas e-Kendra")
common.clickToElement("//p[contains(text(),'Account Details')]")
common.switchWindowByTitle("Welcome to HDFC Bank NetBanking")
common.switchToIframe("//frame[@name='footer']")
common.clickToElement("//a[text()='Privacy Policy']")
common.switchToDefaultContent()
common.switchWindowByTitle(
    "HDFC Bank - Leading Bank in India, Banking Services, Private Banking, Personal Loan, Car Loan")
common.clickToElement("//a[@href='/csr/index.aspx']")
common.quitBrowser()
