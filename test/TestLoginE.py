import inspect
import pytest
import sys
sys.path.append('../page/')
sys.path.append('../common/')

import WebDriverFactory,DataProvider,AbstractSelenium,LoginPage

class TestLogin(AbstractSelenium.AbstractSelenium):

    @pytest.mark.parametrize("TC_ID,TC_NAME,userName,userPass",DataProvider.DataProvider.getData("test_verifyLoginForValidUser"))
    def test_verifyLoginForValidUser(self,TC_ID,TC_NAME,userName,userPass):
        print("*********** in test1",userName,userPass)
        LoginPage.LoginPage().navigateToLoginPage().loginForValidUser(userName,userPass)
