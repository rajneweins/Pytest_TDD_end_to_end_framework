import time

from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_clickable_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def click(self, locator):
        try:
            element = self.find_element(locator)
            element.click()
            time.sleep(3)
        except ElementNotInteractableException:
            time.sleep(2)
            element = self.find_element(locator)
            self.driver.execute_script('arguments[0].click();', element)
            time.sleep(3)

    def type_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def _upload_file(self, locator, doc):
        # browse and upload files
        self.find_element(locator)
        # file_path = os.path.join(os.getcwd(), doc)
        self.find_element(locator).send_keys(doc)
        time.sleep(3)
