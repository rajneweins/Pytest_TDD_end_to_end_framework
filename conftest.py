import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from resources.config import Config
from test.utils.cluster_utils import Cluster
from test.utils.databricks_utils import DatabricksDBUtils


# Database connection setup
@pytest.fixture(scope="session")
def databricks_connection():
    utils = DatabricksDBUtils(Config.WORKSPACE_URL, Config.DATABRICKS_TOKEN, Config.CLUSTER_ID)
    # start cluster
    while True:
        if utils.start_cluster() != 'RUNNING':
            time.sleep(60)
        else:
            break
    server_name = Config.SERVER_HOSTNAME
    http_path = Config.HTTP_PATH
    db_user = Config.USERNAME
    db_password = Config.DATABRICKS_TOKEN
    driver = Config.DRIVER
    port = Config.PORT
    ssl_ca = Config.SSL_CA

    # Create an instance of DatabricksDBUtils
    # utils = DatabricksDBUtils()
    utils.conn_param(server_name, http_path, db_user, db_password, driver, port, ssl_ca)
    utils.connect()
    yield utils
    utils.disconnect()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="Specify the browser type: chrome or firefox")
    parser.addoption("--headless", action="store", default="False",
                     help="specify if headless mode is needed")
    parser.addoption('--report', type=str, default='reports/report.html',
                     help='HTML report path')


# Driver Setup
@pytest.fixture(scope="session")
def browser(request):
    cluster_instance = Cluster(Config.WORKSPACE_URL, Config.DATABRICKS_TOKEN, Config.CLUSTER_ID)
    # start cluster
    while True:
        if cluster_instance.start_cluster() != 'RUNNING':
            time.sleep(60)
        else:
            break
    browser_type = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    if browser_type.lower() == "chrome":
        # Set up the Chrome browser driver
        options = webdriver.ChromeOptions()
        if headless.lower() == "true":
            options.add_argument("--headless")
        # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        path = 'resources/drivers/chromedriver.exe'
        driver = webdriver.Chrome(service=Service(executable_path=path), options=options)
    elif browser_type.lower() == "firefox":
        # Set up the Firefox browser driver
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Invalid browser type: {browser_type}")

    # Set up the implicit wait time for the driver
    driver.implicitly_wait(10)
    # Pass the driver instance to the tests
    driver.maximize_window()
    yield driver
    # Quit the driver after the tests
    driver.quit()
