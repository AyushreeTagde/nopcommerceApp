# page object class for login page

class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//body/div[6]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/input[1]"
    link_logout_linktext = "Logout"

    # we have written all the locator in one place, now action method for all locator.
    # need to initialize the driver to perform action on that locator. For that we need to create one constructor
    # (constructor - to initialize driver)
    # it will automatically invoke during object creation

    def __init__(self,driver):  # so this driver will come from actual test case
        self.driver=driver  # this self.driver we are going to use to invoke all the above statement.

        #  action methods for every locator
    def setusername(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)
    def setpassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
    def clicklogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
    def clicklogout(self):
        self.driver.find_element_by_link_text(self.link_logout_linktext).click()

