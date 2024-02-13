from selenium.webdriver.common.by import By


class LoginLocators:
    TITLE = (By.XPATH, '//a[@title="Microsoft Azure"]')
    USERNAME_INPUT = (By.XPATH, "//input[@type='email']")
    #PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    PASSWORD_INPUT=(By.XPATH,"//input[contains(@name,'passwd')and contains(@type,'password')]")
    NEXT_BUTTON = (By.XPATH, "//input[@type='submit']")
    SIGNIN_BUTTON = (By.XPATH, "//input[contains(@type,'submit') and contains(@data-report-trigger,'click')]")
    # SIGNIN_BUTTON = (By.ID, 'idSIButton9')
    LOGOUT_BUTTON = (By.ID, '')
