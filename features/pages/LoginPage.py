from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.baseURL = "https://www.saucedemo.com/"
        self.user = "user-name"
        self.password = "password"
        self.login_button = "login-button"

    def get_user(self):
        return self.driver.find_element(By.ID, self.user)

    def get_password(self):
        return self.driver.find_element(By.ID, self.password)

    def get_button_login(self):
        return self.driver.find_element(By.ID, self.login_button)

    def click_login(self):
        self.get_button_login().click()

    def send_user(self, user):
        self.get_user().send_keys(user)

    def send_password(self, password):
        self.get_password().send_keys(password)

