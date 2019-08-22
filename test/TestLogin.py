import inspect
import pytest
import sys
sys.path.append('../page/')
sys.path.append('../common/')

import WebDriverFactory,DataProvider,AbstractSelenium,LoginPage

class TestLogin(AbstractSelenium.AbstractSelenium):    #file.class

    @pytest.mark.parametrize("userName", [("vzodge")])
    def test_verifyLoginForExpiredUser(self,userName):      #self=this
        print("*********** in test1",userName)
        LoginPage.LoginPage().navigateToLoginPage().loginForExpiredPassword(userName).printErrorMessage()
                                                    # .navigatetologin(username n pswrd)
    @pytest.mark.parametrize("userName", [("vaibhavz"),("zodge")])            #"UserName, password" , [("admin , admin")]
    def test_verifyLoginForInvalidUser(self,userName):                        #def= definition
        print("*********** in test1",userName)
        LoginPage.LoginPage().navigateToLoginPage().loginForInvalidUser(userName)
                                                      #static class.method
    @pytest.mark.parametrize("TC_ID,TC_NAME,userName",DataProvider.DataProvider.getData("test_verifyLoginForInvalidUser"))
    def test_verifyLoginForInvalidUser(self,TC_ID,TC_NAME,userName):
        print("*********** in test1",userName)
        LoginPage.LoginPage().navigateToLoginPage().loginForInvalidUser(userName)
