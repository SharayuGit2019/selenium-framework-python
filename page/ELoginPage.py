import WebDriverFactory
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import BasePage

class LoginPage(BasePage.BasePage):
		       
	
	elmUserName=(By.ID,"txtUsername")
	elmUserPass=(By.ID,"txtPassword")
	elmLoginButton=(By.ID,"btnLogin")                                                        
	                                                             
	             
	def __init__(self):
		self.wait=WebDriverWait(WebDriverFactory.WebDriverFactory.getDriver(),20)
		self.driver=WebDriverFactory.WebDriverFactory.getDriver()
		
	def navigateToLoginPage(self):
		self.driver.get("http://127.0.0.1/orangehrm-3.3.1/symfony/web/index.php/admin/viewSystemUsers?sortField=user_name&sortOrder=ASC")
		return self
		
	def __login(self,userName,userPass):
		self.findElementBy(self.elmUserName).send_keys(userName)
		self.findElementBy(self.elmUserPass).send_keys(userPass)
		self.findElementBy(self.elmLoginButton).click()
		return self 

	
