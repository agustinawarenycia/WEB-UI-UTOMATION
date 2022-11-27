from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.header_title = "title"
        self.baseURL = "https://www.saucedemo.com/inventory"

    def get_header_title(self):
        return self.driver.find_element(By.CLASS_NAME, self.header_title)

    def get_text_header_title(self):
        return self.get_header_title().text
