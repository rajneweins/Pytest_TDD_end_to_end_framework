from selenium.webdriver.common.by import By


class HomePageLocators:
    #HOME_BUTTON = (By.XPATH, "(//a[@href='#home'])[1]")
    #HOME_BUTTON=(By.XPATH,"(//a[contains(@class,'fxs-breadcrumb-crumb fxs-portal-text fxs-breadcrumb-crumb-active')])[1]")
    #HOME_BUTTON=(By.XPATH,"(//a[contains(@href,'#home') and contains(@class,'fxs-breadcrumb-crumb fxs-portal-text fxs-breadcrumb-crumb-active')]")
    HOME_BUTTON=(By.XPATH,"//nav[contains(@class,'fxs-breadcrumb-wrapper')]")
    # Azure Applications Locators
    PRIVILIGED_LICENSE = (By.XPATH, "//div[contains(text(),'Microsoft Entra Privileged Identity Management')]")
    #RESOURCE_GROUPS = (By.XPATH, "//div[contains(text(),'Resource groups')]")
    RESOURCE_GROUPS=(By.XPATH,"//div[contains(text(),'Resource groups') and contains(@class,'fxs-portal-text fxs-home-feature-name')]")


class LicenseLocators(HomePageLocators):
    MY_ROLES = (By.XPATH, "//div[normalize-space()='My roles']")
    #AZURE_RESOURCE = \
        #(By.XPATH, '(//div[@data-telemetryname="Menu-azurerbac" and contains(text(), "Azure resources")])[2]')
    AZURE_RESOURCE = \
        (By.XPATH,"(//div[contains(@class,'ext-fxc-menu-listView-item') and contains(text(),'Azure resources')])[2]")
    ELIGIBLE_ASSIGN = (By.XPATH, "(//span[contains(text(),'Eligible assignments')])[1]")
    ACTIVE_ASSIGN = (By.XPATH, "(//span[contains(text(),'Active assignments')])[1]")
    ACTIVATED_STATUS = (By.XPATH, "//div[contains(text(),'Activated')]")
    ACTIVATE_BUTTON = (By.XPATH, "//a[normalize-space()='Activate']")
    DURATION_INPUT = \
        (By.XPATH, "(//label[contains(text(), 'Duration (hours)')]/parent::div/following-sibling::div//input)[2]")
    REASON_INPUT = \
        (By.XPATH, "//label[contains(text(), 'Reason (max 500 characters)')]/parent::div/following-sibling::div//textarea")
    ACTIVATE_BTN = (By.XPATH, "//div[@title='Activate']")


class ResourceGroupsLocators(HomePageLocators):
    # common locators
    # RESOURCE_CONTAINER_STG = (By.XPATH, "(//a[contains(@href, '/resourceGroups/rg-premsvcs-tst9-eastus-009')])[6]")
    RESOURCE_CONTAINER_STG = (By.XPATH, "(//a[contains(@href, '/resourceGroups/rg-premsvcs-t160-eastus-160') and text()= 'rg-premsvcs-t160-eastus-160'])[1]")
    # upload file locators
    # CONTAINER_GROUP = (By.XPATH, "(//a[contains(@href, '/storageAccounts/ststagingtst9eastus009')])[2]")
    CONTAINER_GROUP = (By.XPATH, "//a[contains(@href, '/storageAccounts/ststagingt160eastus160')]")
    CONTAINER = (By.XPATH, "//div[@data-telemetryname='Menu-containersList']")
    #CONATINER=(By.XPATH,"(//a[contains(@class,'fxc-gcflink-link') and contains(text(),'ststagingt160eastus160')])[1]")
    CONTAINER_TEST = (By.XPATH, "//div[contains(text(),'test')]")
    UPLOAD_BTN = (By.XPATH, '//div[@data-telemetryname="Command-UploadBlob"]')
    B_IFRAME = (By.XPATH, "//h2[contains(text(), 'Upload blob')]/ancestor::section/following-sibling::iframe")
    B_IFRAME_2 = (By.XPATH, "(//h2[contains(text(), 'Upload blob')]/ancestor::section/following-sibling::iframe)[2]")
    FILE_INPUT_ELE = (By.XPATH, "//input[@type='file']")
    OVERWRITE_CHECKBOX = (By.XPATH, '//i[@data-icon-name="CheckMark"]')
    UPLOAD_BUTTON = (By.XPATH, '//button[@name="Upload"]')

    # Azure data factory locators
    ADF_CONTAINER_STG = (By.XPATH, "(//a[contains(@href, '/resourceGroups/rg-premsvcs-t160-eastus-160') and text()= 'rg-premsvcs-t160-eastus-160'])")
    ADF_GROUP = (By.XPATH, "(//a[contains(@href, '/factories/adf-premsvcs-t160-eastus-160')])")
    RESOURCE_ADF = (By.XPATH, "(//a[normalize-space()='adf-premsvcs-t160-eastus-160'])")
    LAUNCH_STUDIO = (By.XPATH, "//p[@class='ext-launch-link']")
    MONITOR_ICON = (By.XPATH, "//div[@class='adfNavIcon icon svg-monitoring-icon ng-star-inserted']")
    IN_PROGRESS_ICON = (By.XPATH, '//div[@aria-label="Status In progress"]')
    # LOAD_RSA_BUTTON = \
    #     (By.XPATH, '//div[@aria-label="Status In progress"]/ancestor::td/preceding-sibling::td/div[@aria-label="Pipeline name LoadRSA"]')
    LOAD_RSA_BUTTON = (By.XPATH, "(//span[contains(text(), 'LoadRSA')])[1]")
    REFRESH_BUTTON = (By.XPATH, "//div[@class='control-context'][normalize-space()='Refresh']")
    ALL_PIPELINE_RUNS_LINK = (By.XPATH, "//div[@aria-label='Navigate back to All pipeline runs']")

    LOAD_RSA_STATUS = \
        (By.XPATH,
         "//div[contains(text(), 'LoadRSA - Activity runs')]/preceding-sibling::div/div")
    # LAUNCH_WORKSPACE=(By.XPATH,"//div[@data-bind='text: launchWorkspaceLabel']")
    # WORKSPACE=(By.XPATH,"//span[@class='css-a5qyws'][normalize-space()='Workspace']")
    # WORKSPACE_FOLDER=
    # USERS=
    # DEV_CLUSTER=("By.XPATH,//span[@class='webapp-css-1h52dri']")
    # DEV_CLUSTER1=("By.XPATH,//span[@class='anticon webapp-css-dzwpit']//*[name()='svg']")
    # DETACH_REATACH=("By.XPATH,//div[normalize-space()='Detach & re-attach']")
    # CONFIRM_BTN=("By.XPATH,//span[normalize-space()='Confirm']")
    # INSERT_NEW_CELL_BTN=("By.XPATH,//body/div[@id='app-root']/div[@id='legacy-app-root']/div[@id='overallView']/div/div[@id='content']/div[@class='webapp-css-ho1qnd']/div[@class='webapp-css-jp9wdj']/main[@class='ant-layout-content']/uses-legacy-bootstrap[@data-wrapped-element-id='CommandListView']/div[@class='new-notebook overallContainer']/div[@class='shell-top new-notebook webapp-css-0']/div[2]/div[1]/div[1]/a[1]/i[1]")

    #RUN_CELL=("By.XPATH,//div[contains(@class,'new-notebook command mainCommand apply-box-shadow apply-hover-box-shadow command-input cellIndex-1 cell-3272668792279683-1042249242373413 webapp-css-34ysdq')]//i[contains(@class,'fa fa-play fa-fw')]")
