from selenium import webdriver

class WebDriverFactory:

	def setDriver():
		WebDriverFactory.driver = webdriver.Chrome("C:\Selenium\chromedriver.exe") #set driver object to static driver object
		
	def getDriver():
		return WebDriverFactory.driver
