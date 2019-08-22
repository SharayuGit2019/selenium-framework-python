import inspect
import pytest
import sys
sys.path.append('../page/')
sys.path.append('../common/')

import WebDriverFactory,DataProvider,AbstractSelenium,OLoginPage

class TestOLogin(AbstractSelenium.AbstractSelenium):

    @pytest.mark.parametrize('userName,userPass',[('admin','admin')])
    def test_verifyAdminLoginSucc(self,userName,userPass):
        print("*********** in test1",userName,userPass)
        OLoginPage.OLoginPage().navigateToLoginPage().loginForValidAdminUser(userName,userPass)
