from selenium.common import StaleElementReferenceException

from resources.config import Config
from test.locators.login_locators import LoginLocators as ll
from test.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def go_to_login_page(self):
        self.driver.get(Config.LOGIN_URL)

    def enter_username(self, username):
        username_input = self.find_element(ll.USERNAME_INPUT)
        username_input.clear()
        username_input.send_keys(username)

    def click_next_button(self):
        next_button = self.find_clickable_element(ll.NEXT_BUTTON)
        next_button.click()

    def click_signin_button(self):
        signin_button = self.find_clickable_element(ll.SIGNIN_BUTTON)
        signin_button.click()

    def enter_password(self, password):
        password_input = self.find_element(ll.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

    def is_login_successful(self):
        welcome_message = self.find_element(ll.TITLE)
        return welcome_message.text

    def click_logout_button(self):
        logout_button = self.find_element(ll.LOGOUT_BUTTON)
        logout_button.click()
