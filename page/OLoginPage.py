import WebDriverFactory
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import BasePage

class OLoginPage(BasePage.BasePage):
		       
	elmUserName=(By.ID,"txtUsername")
	elmUserName=(By.ID,"txtPassword")
	elmLoginButton=(By.ID,"btnLogin")
	
	def __init__(self):
		self.wait=WebDriverWait(WebDriverFactory.WebDriverFactory.getDriver(),20)
		self.driver=WebDriverFactory.WebDriverFactory.getDriver()
		
	def navigateToLoginPage(self):
		self.driver.get("http://127.0.0.1/orangehrm-3.3.1/symfony/web/index.php/admin/viewSystemUsers?sortField=user_name&sortOrder=ASC")
		return self
		
	def loginForValidAdminUser(self,strUserName,strUserPass):
		self.findElementBy(self.elmUserName).send_keys(strUserName)
		self.findElementBy(self.elmUserName).send_keys(strUserPass)
		self.findElementBy(self.elmLoginButton).click()
		return self


