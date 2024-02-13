import os
import time
from selenium.webdriver.common.by import By
from test.pages.login_page import LoginPage
from test.locators.homepage_locators import LicenseLocators as lil, ResourceGroupsLocators as rgl
from selenium.common.exceptions import TimeoutException


class HomePage(LoginPage):
    def __init__(self, driver):
        super().__init__(driver)

    def activate_license(self, duration=8, input_text=None):
        global b
        b = None
        self.click(lil.PRIVILIGED_LICENSE)
        self.click(lil.MY_ROLES)
        self.click(lil.AZURE_RESOURCE)
        while True:
            self.click(lil.ACTIVE_ASSIGN)
            time.sleep(60)
            if not self.is_element_present(lil.ACTIVATED_STATUS):
                self.click(lil.ELIGIBLE_ASSIGN)
                time.sleep(2)
                self.click(lil.ACTIVATE_BUTTON)
                time.sleep(2)
                self.find_clickable_element(lil.DURATION_INPUT)
                self.type_text(lil.DURATION_INPUT, duration)
                self.type_text(lil.REASON_INPUT, input_text)
                self.click(lil.ACTIVATE_BTN)
                time.sleep(30)
                b = False
            else:
                b = True
                break
        return b

    def upload_files_in_container(self, list_of_files=None):
        """add parquet files along with success file"""
        try:
            self.click(rgl.HOME_BUTTON)
        except:
            pass
        self.click(rgl.RESOURCE_GROUPS)
        try:
            self.click(rgl.RESOURCE_CONTAINER_STG)
        except:
            _locator = (By.XPATH, "(//a[contains(@href, '/resourceGroups/rg-premsvcs-tst5-eastus-005') and text()= "
                                  "'rg-premsvcs-tst5-eastus-005'])")
            self.click(_locator)
        self.click(rgl.CONTAINER_GROUP)
        self.click(rgl.CONTAINER)
        self.click(rgl.CONTAINER_TEST)

        for i in range(len(list_of_files)):
            self.click(rgl.UPLOAD_BTN)
            time.sleep(2)
            # Switch to the iframe
            IFRAME_LOC = (By.XPATH, f"(//h2[contains(text(), 'Upload "
                                    f"blob')]/ancestor::section/following-sibling::iframe)[{i + 1}]")
            try:
                if self.find_element(IFRAME_LOC):
                    iframe_element = self.find_element(IFRAME_LOC)
                    self.driver.switch_to.frame(iframe_element)
            except TimeoutException:
                time.sleep(30)
                iframe_element = self.find_element(IFRAME_LOC)
                self.driver.switch_to.frame(iframe_element)
            self.click(rgl.OVERWRITE_CHECKBOX)
            self._upload_file(rgl.FILE_INPUT_ELE, list_of_files[i])
            # upl.send_keys(i)
            self.click(rgl.UPLOAD_BUTTON)
            time.sleep(1)
            self.driver.switch_to.default_content()
            print(f"File {list_of_files[i]} successfully added into the container")
        print("Verifying in progress, if files loaded successfully into bronze DB")

    def process_file(self):
        try:
            self.click(rgl.HOME_BUTTON)
        except:
            pass
        self.click(rgl.RESOURCE_GROUPS)
        self.click(rgl.ADF_CONTAINER_STG)
        self.click(rgl.ADF_GROUP)
        self.click(rgl.LAUNCH_STUDIO)

        self.driver.switch_to.window(self.driver.window_handles[1])
        time.sleep(5)
        try:
            self.click(rgl.MONITOR_ICON)
        except:
            self.click(rgl.MONITOR_ICON)
        self.click(rgl.LOAD_RSA_BUTTON)
        time.sleep(5)
        while True:
            if 'Failed' in self.find_element(rgl.LOAD_RSA_STATUS).get_attribute('class'):
                assert True
                print("Parquet files are uploaded successfully into bronze.")
                break
            else:
                time.sleep(30)
                self.click(rgl.ALL_PIPELINE_RUNS_LINK)
                self.click(rgl.LOAD_RSA_BUTTON)
