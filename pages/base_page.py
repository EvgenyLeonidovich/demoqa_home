from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.saucedemo.com/'
    def visit(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def visit_name(self):
        return self.driver.get(self.base_url)

    def find_element_name(self, locator_name):
        return self.driver.find_element_name(By.CSS_SELECTOR, locator_name)

    def visit_password(self):
        return self.driver.get(self.base_url)

    def find_element_password(self, locator_password):
        return self.driver.find_element_password(By.CSS_SELECTOR, locator_password)