from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
class SwagLabs(BasePage):
    def exist_icon(self):
        try:
            self.find_element(locator= 'div.login_logo')
        except NoSuchElementException:
            return False
        return True

    def exist_icon_name(self):
        try:
            self.find_element_name(locator_name='div > form > div:nth-child(1)')
        except NoSuchElementException:
            return False
        return True

    def exist_icon_password(self):
        try:
            self.find_element_password(locator_password='div > form > div:nth-child(2)')
        except NoSuchElementException:
            return False
        return True