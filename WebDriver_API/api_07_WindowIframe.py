from selenium import webdriver

driver = webdriver.Chrome("E:\Python WebDriver\Ex1\WebdriverAPI\Driver\chromedriver.exe")
driver.get("http://www.hdfcbank.com/")
driver.maximize_window()

parentWindow = driver.current_window_handle
driver.find_element_by_xpath("//a[@href='/htdocs/common/agri/index.html']").click()
allAgriWindow = driver.window_handles

for handleAgri in allAgriWindow:
    driver.switch_to.window(handleAgri)
    titleWindow = driver.title
    if titleWindow == "HDFC Bank Kisan Dhan Vikas e-Kendra":
        break

driver.find_element_by_xpath("//p[contains(text(),'Account Details')]").click()
allAccountWindow = driver.window_handles

for handleAccount in allAccountWindow:
    driver.switch_to.window(handleAccount)
    titleAccountWindow = driver.title
    if titleAccountWindow == "Welcome to HDFC Bank NetBanking":
        break

iframeLabel = driver.find_element_by_xpath("//frame[@name='footer']")
driver.switch_to.frame(iframeLabel)
driver.find_element_by_xpath("//a[text()='Privacy Policy']").click()
driver.switch_to.default_content()

allHDFCBankWindow = driver.window_handles

for handleHDFCBank in allHDFCBankWindow:
    driver.switch_to.window(handleHDFCBank)
    titleHDFCBankWindow = driver.title
    if titleHDFCBankWindow == "HDFC Bank - Leading Bank in India, Banking Services, Private Banking, Personal Loan, Car Loan":
        break

driver.find_element_by_xpath("//a[@href='/csr/index.aspx']").click()
print("Current title = " + driver.title)
driver.quit()
