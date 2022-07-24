import pytest
from appium import webdriver
import src.helpers.CustomLogger as cl
import allure
from src.base.DriverDevice import DriverDevice

desired_caps = {} 
desired_caps['platformName'] = 'ios' 
desired_caps['platformVersion'] = '15.5'
desired_caps['automationName'] = 'XCUITest'
desired_caps['deviceName'] = 'iPhone 13 Pro Max'
# desired_caps['app'] = ('/Users/jcgularte/Downloads/BetterVet-QA.apk') 
desired_caps['autoWebview'] = 'true' 
desired_caps['browserName'] = 'safari'
desired_caps['startIWDP'] = 'true'

@pytest.fixture()
def init_driver(request, device):
    # log = cl.customLogger()
    deviceObject = DriverDevice(device)
    driver = deviceObject.createDriverSession()
    request.cls.driver = driver
    with allure.step("LAUNCHING APP"):
        print("TEST HAS STARTED")
        yield
        print("TEST HAS FINISHED")
        # driver.quit()

def pytest_addoption(parser): #method to add commands specifications
    parser.addoption("--device", help="Type of browser to use for the execution")

@pytest.fixture(scope="session")
def device(request):
    return request.config.getoption("--device")