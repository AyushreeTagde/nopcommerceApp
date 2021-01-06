# test case for login
import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from PageObjects.LoginPage import Login
from Utilities.readproperties import readconfig
from Utilities.customLogger import LogGen

@allure.severity(allure.severity_level.NORMAL)
class Test_001_Login:
    baseURL = readconfig.getURL()
    username = readconfig.getuseremail()
    password = readconfig.getuserpassword()
    # baseURL = "https://admin-demo.nopcommerce.com"
    # username = "admin@yourstore.com"
    # password = "admin"

    logger = LogGen.loggen()


    @pytest.mark.regression
    @allure.severity(allure.severity_level.MINOR)
    def test_homepageTitle(self,setup):
        self.logger.info("******** Test_001 Login ******")
        self.logger.info("******* Verifying home page title ********")
        # self.driver=webdriver.Chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********* home page title test is passed ********")

        else:
            allure.attach(self.driver.get_screenshot_as_png(),name="testhomepagetitle", attachment_type=AttachmentType.PNG)
            self.driver.close()
            self.logger.error("***** home page title test is failed ******")

            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    @allure.severity(allure.severity_level.BLOCKER)

    def test_login(self,setup):
        self.logger.info("********** Verifying Login test ***********")

        self.driver = setup
        self.driver.get(self.baseURL)
        # now need to create object of ba
        # se class (means we call the Login)
        self.lp = Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title

        if act_title=="Dashboard / nopCommerce administration13":
            assert True
            self.driver.close()
            self.logger.info("****** Login test is passed ******")


        else:
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            allure.attach(self.driver.get_screenshot_as_png(),name="testloginpage", attachment_type=AttachmentType.PNG)

            self.driver.close()
            self.logger.error("********* Login test is failed **********")

            assert False


