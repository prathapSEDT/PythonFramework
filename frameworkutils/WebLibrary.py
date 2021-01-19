from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from configparser import ConfigParser

def getConfigDetails(sectionname,value):
    print("Getting config details")
    config=ConfigParser()
    filepath="../configuration/application-properties.cnf"
    config.read(filepath)
    return config.get(sectionname,value)

def launchBrowser():
    global driver
    url=getConfigDetails("APPLICATION_DETAILS","APP_URL")
    browserType=getConfigDetails("BROWSER_DETAILS","EXECUTE")
    if str(browserType).lower()=="chrome":
        execPath = "../drivers/chromedriver"
        caps = DesiredCapabilities.CHROME
        caps["chromeOptions"] = {}
        caps["chromeOptions"]["excludeSwitches"] = ["disable-popup-blocking"]
        driver = webdriver.Chrome(executable_path=execPath,desired_capabilities=caps)
    elif str(browserType).lower()=="firefox":
        execPath = "../drivers/geckodriver"
        driver = webdriver.Firefox(executable_path=execPath)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    return driver

def clickElement(driver,xpath):
    driver.find_element_by_xpath(xpath).click()

def sendData(driver,xpath,data):
    driver.find_element_by_xpath(xpath).clear()
    driver.find_element_by_xpath().send_keys(data)

def elementExists(driver,xpath):
    status=True
    try:
        driver.find_element_by_xpath(xpath).is_displayed()
    except Exception as e:
        print(e)
        status=False
    return status

def getElementText(driver,xpath):
    return driver.find_element_by_xpath(xpath).text





